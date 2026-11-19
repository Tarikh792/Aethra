
import io
import hashlib
import streamlit as st

from pdf_reader import extract_text
from chunker import split_text
from embeddings import create_embeddings
from rag import ask_aethra


# PAGE SETTINGS
st.set_page_config(
    page_title="Aethra | Document Intelligence",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)


# PREMIUM DARK BLUE STYLING
st.markdown("""
<style>
    .stApp {
        background: #080f20;
        color: #e2e8f0;
    }

    [data-testid="stSidebar"] {
        background: #0e1930;
        border-right: 1px solid #223654;
    }

    [data-testid="stSidebar"] * {
        color: #e2e8f0;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2.5rem;
        padding-bottom: 5rem;
    }

    .aethra-logo {
        font-size: 2.8rem;
        font-weight: 800;
        color: #f8fafc;
        letter-spacing: -1.5px;
        margin-bottom: 0;
    }

    .aethra-subtitle {
        color: #94a3b8;
        font-size: 1rem;
        margin-bottom: 1.8rem;
    }

    .hero-card {
        background: linear-gradient(
            135deg, #122747, #0c1932
        );
        border: 1px solid #284b78;
        border-radius: 18px;
        padding: 26px;
        margin: 20px 0;
    }

    .hero-title {
        color: #f8fafc;
        font-size: 1.35rem;
        font-weight: 700;
    }

    .hero-text {
        color: #a9bad5;
        margin-top: 8px;
    }

    .document-card {
        background: #102b30;
        border: 1px solid #20685e;
        border-radius: 12px;
        padding: 16px 20px;
        color: #a7f3d0;
        margin-bottom: 18px;
    }

    [data-testid="stChatMessage"] {
        background: #101c32;
        border: 1px solid #233954;
        border-radius: 15px;
        padding: 16px;
        margin-bottom: 12px;
    }

    [data-testid="stChatInput"] {
        background: #12213b;
        border-radius: 14px;
    }

    .stButton > button {
        background: #1d4ed8;
        color: white;
        border: 1px solid #3b82f6;
        border-radius: 10px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background: #2563eb;
        color: white;
        border-color: #60a5fa;
    }

    [data-testid="stFileUploader"] {
        background: #101f37;
        border-radius: 12px;
        padding: 8px;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        margin-top: 35px;
    }
</style>
""", unsafe_allow_html=True)


# DOCUMENT PROCESSING
@st.cache_data(show_spinner=False)
def process_document(pdf_bytes):
    pdf_file = io.BytesIO(pdf_bytes)
    text = extract_text(pdf_file)

    if not text.strip():
        raise ValueError(
            "No readable text found in this PDF."
        )

    chunks = split_text(text)
    vectors = create_embeddings(chunks)

    return chunks, vectors


# SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_id" not in st.session_state:
    st.session_state.document_id = None


# SIDEBAR
with st.sidebar:
    st.markdown("## 💎 Aethra")
    st.caption("YOUR AI RESEARCH WORKSPACE")

    st.divider()

    st.markdown("#### 📄 Your Document")

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if st.button(
        "＋ New Chat",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("#### ✨ Features")
    st.markdown(
        """
        - PDF Question Answering
        - Semantic Search
        - Context-Aware Responses
        - Source Chunk References
        """
    )

    st.divider()
    st.caption("Powered by Groq + Sentence Transformers")
    st.caption("Aethra • Version 1.0")


# MAIN HEADER
st.markdown(
    '<div class="aethra-logo">💎 Aethra</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="aethra-subtitle">'
    'Intelligence for every document.'
    '</div>',
    unsafe_allow_html=True
)


# DOCUMENT WORKSPACE
if uploaded_file is not None:

    pdf_bytes = uploaded_file.getvalue()
    document_id = hashlib.sha256(
        pdf_bytes
    ).hexdigest()

    if st.session_state.document_id != document_id:
        st.session_state.document_id = document_id
        st.session_state.messages = []

    try:
        with st.spinner("Analyzing your document..."):
            chunks, vectors = process_document(pdf_bytes)

    except Exception as error:
        st.error(f"Document processing failed: {error}")
        st.stop()

    st.markdown(
        '<div class="document-card">'
        '✓ Document processed and ready for questions'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"**📄 Current PDF:** {uploaded_file.name}")

    with st.expander("View Document Intelligence"):
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Text Chunks", len(chunks))

        with col2:
            st.metric(
                "Vector Dimensions",
                vectors.shape[1]
            )

    st.divider()

    if not st.session_state.messages:
        st.markdown("""
        <div class="hero-card">
            <div class="hero-title">
                Your document is ready ✨
            </div>
            <div class="hero-text">
                Ask questions, explore concepts, and
                discover information inside your PDF.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Try asking:**")
        st.caption("• What is this document about?")
        st.caption("• Summarize the main points.")
        st.caption("• Explain the key concepts.")

    # DISPLAY CHAT HISTORY
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # USER INPUT
    question = st.chat_input(
        "Ask anything about your document..."
    )

    if question:
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            try:
                with st.spinner(
                    "Searching your document..."
                ):
                    answer = ask_aethra(
                        question,
                        chunks,
                        vectors
                    )

                if not answer:
                    answer = (
                        "I couldn't generate an answer. "
                        "Please try again."
                    )

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                st.error(
                    f"Unable to generate an answer: {error}"
                )

else:
    st.markdown("""
    <div class="hero-card">
        <div class="hero-title">
            Welcome to Aethra
        </div>
        <div class="hero-text">
            Transform your PDFs into an interactive
            knowledge experience.
            <br><br>
            Upload a document from the sidebar
            to start exploring with AI.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("📄 Upload Documents")

    with col2:
        st.info("🔍 Semantic Retrieval")

    with col3:
        st.info("💬 AI-Powered Answers")


# FOOTER
st.markdown("""
<div class="footer">
    AETHRA — DOCUMENT INTELLIGENCE ENGINE
</div>
""", unsafe_allow_html=True)
