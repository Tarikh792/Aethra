import numpy as np
from embeddings import model


def search_chunks(query, chunks, vectors, top_k=3):
    query_vector = model.encode([query])[0]

    # Cosine similarity calculate karo
    numerator = np.dot(vectors, query_vector)

    denominator = (
        np.linalg.norm(vectors, axis=1)
        * np.linalg.norm(query_vector)
    )

    scores = numerator / np.maximum(denominator, 1e-10)

    # Sabse relevant chunks select karo
    top_indices = np.argsort(scores)[::-1][:top_k]

    return [
        {
            "text": chunks[i],
            "score": float(scores[i]),
            "chunk_id": int(i)
        }
        for i in top_indices
    ]
    
if __name__ == "__main__":
    from pdf_reader import extract_text
    from chunker import split_text
    from embeddings import create_embeddings

    text = extract_text("sample.pdf")
    chunks = split_text(text)
    vectors = create_embeddings(chunks)

    results = search_chunks(
        "What is research design?",
        chunks,
        vectors
    )

    for result in results:
        print("\nChunk:", result["chunk_id"])
        print("Similarity:", round(result["score"], 3))
        print("Text:", result["text"][:300])
    