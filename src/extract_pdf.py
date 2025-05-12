import fitz  # PyMuPDF

def extract_text_chunks_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []

    # Extrahiere die Metadaten des PDFs
    pdf_metadata = doc.metadata
    pdf_title = pdf_metadata.get("title", "Unbekannter Titel")  # Titel aus den Metadaten
    pdf_author = pdf_metadata.get("author", "Unbekannter Autor")  # Autor aus den Metadaten

    for page_num, page in enumerate(doc):
        text = page.get_text()

        # Entferne die Seitenzahl aus dem Text, falls vorhanden
        page_number_str = str(page_num + 1)  # menschenlesbare Seitenzahl
        if text.startswith(page_number_str):  # Prüfe, ob der Text mit der Seitenzahl beginnt
            text = text[len(page_number_str):].strip()  # Entferne die Seitenzahl

        chunks.append({
            "text": text,
            "metadata": {
                "page": page_num + 1,  # menschenlesbare Seitenzahl
                "title": pdf_title,  # Titel aus den Metadaten hinzufügen
                "author": pdf_author  # Autor aus den Metadaten hinzufügen
            }
        })

    return chunks
