from groq import Groq
import streamlit as st
from retriever import search_chunks

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def ask_aethra(question, chunks, vectors):
    results = search_chunks(question, chunks, vectors, top_k=5)

    context = "\n\n".join(
        f"[Source {r['chunk_id']}] {r['text']}"
        for r in results
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are Aethra, a document research assistant. "
                    "Answer using ONLY the provided document context. "
                    "If the answer is not present, say you could not "
                    "find it in the document. "
                    "Cite relevant source IDs in your answer."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Document context:\n{context}\n\n"
                    f"Question: {question}"
                )
            }
        ],
        max_completion_tokens=2048
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    from pdf_reader import extract_text
    from chunker import split_text
    from embeddings import create_embeddings

    text = extract_text("sample.pdf")
    chunks = split_text(text)
    vectors = create_embeddings(chunks)

    question = "What is research design?"

    answer = ask_aethra(question, chunks, vectors)

    print("\nQuestion:", question)
    print("\nAethra's Answer:\n", answer)