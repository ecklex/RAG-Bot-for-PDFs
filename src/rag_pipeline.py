import os
import glob
from src.extract_pdf import extract_text_chunks_from_pdf
from src.chunker import chunk_text_with_metadata
from src.embedder import embed_chunks, model
from src.indexer import build_faiss_index, search_index

def load_all_files_from_folder(folder_path):
    chunks = []

    # PDF-Dateien laden
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    for pdf_path in pdf_files:
        filename = os.path.basename(pdf_path)
        raw_pages = extract_text_chunks_from_pdf(pdf_path)
        file_chunks = chunk_text_with_metadata(raw_pages)
        for chunk in file_chunks:
            chunk["metadata"]["filename"] = filename
        chunks.extend(file_chunks)

    return chunks

def filter_relevant_chunks(chunks, user_question, max_chunks=100):
    """
    Priorisiert Chunks basierend auf Schlüsselwörtern in der Benutzeranfrage und Metadaten.
    """
    question_words = set(user_question.lower().split())
    scored_chunks = []

    for chunk in chunks:
        text = chunk["text"].lower()
        metadata = chunk["metadata"]

        # Berechne einen Score basierend auf Schlüsselwörtern
        keyword_score = sum(1 for word in question_words if word in text)

        # Zusätzlicher Score basierend auf Metadaten (z. B. Titel und Autor)
        metadata_score = 0
        if "title" in metadata and metadata["title"].lower() in user_question.lower():
            metadata_score += 5
        if "author" in metadata and metadata["author"].lower() in user_question.lower():
            metadata_score += 5

        # Gesamtbewertung
        total_score = keyword_score + metadata_score
        scored_chunks.append((chunk, total_score))

    # Sortiere die Chunks nach Score (absteigend) und wähle die Top-Chunks aus
    scored_chunks = sorted(scored_chunks, key=lambda x: x[1], reverse=True)
    return [chunk for chunk, score in scored_chunks[:max_chunks]]

def run_rag(folder_path, user_question):
    chunks = load_all_files_from_folder(folder_path)

    # Filtere relevante Chunks basierend auf der Benutzeranfrage und Metadaten
    chunks = filter_relevant_chunks(chunks, user_question)

    embeddings = embed_chunks(chunks)
    index = build_faiss_index(embeddings)

    query_embedding = model.encode([user_question])[0]
    top_indices = search_index(index, query_embedding)

    response = "Diese Stellen könnten dir weiterhelfen:\n\n"

    # Direkt die Ergebnisse aus FAISS verwenden
    for idx in top_indices:
        chunk = chunks[idx]
        metadata = chunk["metadata"]

        author = metadata.get("author", "Unbekannter Autor")
        title = metadata.get("title", "Unbekannter Titel")
        page_or_section = metadata.get("page", metadata.get("section", "unknown"))

        # Begrenze die Länge des Textes auf 1000 Zeichen
        text_snippet = chunk["text"][:1000]
        if len(chunk["text"]) > 1000:
            text_snippet += "..."

        response += f"📄 **{author}: {title}, Seite {page_or_section}:**\n"
        response += f"...{text_snippet}...\n\n---\n\n"

    return response
