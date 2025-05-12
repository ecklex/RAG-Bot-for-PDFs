def chunk_text_with_metadata(pages):
    final_chunks = []

    for page in pages:
        text = page["text"]
        metadata = page["metadata"]

        # Absätze trennen
        paragraphs = text.split("\n\n")
        for para in paragraphs:
            para = para.strip()
            if para:  # nur nicht-leere Absätze
                final_chunks.append({
                    "text": para,
                    "metadata": metadata
                })

    return final_chunks
