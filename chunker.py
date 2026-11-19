def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start = end - overlap

    return chunks

if __name__ == "__main__":
    from pdf_reader import extract_text

    text = extract_text("sample.pdf")
    chunks = split_text(text)

    print("Total chunks:", len(chunks))
    print("\nFirst chunk:\n", chunks[0])