import streamlit as st
from crawler import crawl_website

# Page configuration
st.set_page_config(
    page_title="WebMind AI",
    page_icon="🌐",
    layout="wide"
)

# Title
st.title("🌐 WebMind AI")
st.write("Enter a website URL and crawl its content.")

# Input URL
url = st.text_input(
    "Website URL",
    placeholder="https://example.com"
)

# Max pages option
max_pages = st.slider(
    "Maximum Pages to Crawl",
    min_value=1,
    max_value=50,
    value=10
)

# Crawl button
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

            except Exception as e:
                st.error(f"Error: {str(e)}")
                