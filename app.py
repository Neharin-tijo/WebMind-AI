import streamlit as st

from crawler import crawl_website
from rag import answer_question

# Page configuration
st.set_page_config(
    page_title="WebMind AI",
    page_icon="🌐",
    layout="wide"
)

# Title
st.title("🌐 WebMind AI")
st.write("Crawl a website and ask questions about its content using AI.")

# --------------------
# Website Crawling
# --------------------

url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

max_pages = st.slider(
    "Maximum Pages to Crawl",
    min_value=1,
    max_value=50,
    value=10
)

if st.button("🚀 Crawl Website"):

    if not url:
        st.error("Please enter a valid URL.")
    else:
        with st.spinner("Crawling website..."):

            try:
                pages = crawl_website(url, max_pages=max_pages)

                st.success(f"Successfully crawled {len(pages)} pages!")

                st.info(
                    "Website content has been saved to data/pages.json"
                )

                st.divider()

                for page_url, content in pages.items():

                    with st.expander(page_url):

                        st.write(content[:1000])

                        if len(content) > 1000:
                            st.caption("Showing first 1000 characters")

                st.warning(
                    "After crawling a new website, run 'python embeddings.py' in the terminal to rebuild the vector database."
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")

# --------------------
# Chatbot Section
# --------------------

st.divider()

st.header("💬 Ask Questions About the Website")

question = st.text_input(
    "Ask a Question",
    placeholder="What services does this company provide?"
)

if st.button("Get Answer"):

    if not question:
        st.warning("Please enter a question.")
    else:

        try:

            with st.spinner("Searching website knowledge base..."):

                answer, sources = answer_question(question)

                st.subheader("Answer")
                st.write(answer)

                st.subheader("Sources")

                if sources:
                    for source in sources:
                        st.write(f"• {source}")
                else:
                    st.write("No sources found.")

        except Exception as e:
            st.error(f"Error: {str(e)}")

