from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embeddings(chunks):
    return model.encode(chunks)

if __name__ == "__main__":
    from pdf_reader import extract_text
    from chunker import split_text

    text = extract_text("sample.pdf")
    chunks = split_text(text)
    vectors = create_embeddings(chunks)

    print("Total chunks:", len(chunks))
    print("Embeddings shape:", vectors.shape)
    print("First vector (first 10 values):", vectors[0][:10])