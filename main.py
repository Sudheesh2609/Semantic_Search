import streamlit as st
from io import StringIO
from vector_search import *
import qa
from utils import *

st.header(":red[Semantic] Search Engine")
url = False
query = False
options = st.radio(
    'Choose task',
    ('Ask a question','Update the Database'))

if 'Update the Database' in options:
    url = st.text_input("Enter the url of the document")
    
if 'Ask a question' in options:
    query = st.text_input("Enter your question")

button = st.button("Submit")
  
if button and (url or query):
    if 'Update the Database' in options:
        with st.spinner("Updating Database..."):
            corpusData = scrape_text_from_url(url)
            addData(corpusData,url)
            st.success("Database Updated")
    if 'Ask a question' in options:
        with st.spinner("Searching for the answer..."):
            urls,res = find_match(query,2)
            context= "\n\n".join(res)
            st.expander("Context").write(context)
            prompt = qa.create_prompt(context,query)
            answer = qa.generate_answer(prompt)
            st.success("Answer: "+answer)

st.sidebar.write(f"""
    ### Info

    **Pinecone index name**: *semanticsearch*

    **Vector dimensionality**: *384*

    **Vector Metrics**: *Cosine*

    **Vector Embeddings**: *SentenceTransformer('all-MiniLM-L6-v2')*

    **OpenAI generation model**: *text-davinci-003*

    ---

    ### How it Works

    1. **Update the Database**: If you choose the "Update the Database" option, enter the URL of the document you want to add to the search index. The text content of the document will be scraped, processed, and added to the search index using Pinecone.

    2. **Ask a Question**: If you choose the "Ask a Question" option, enter your question in the provided text input. The system will search the indexed documents for the most relevant answers using semantic search. The context of the matching documents will be displayed, and an answer will be generated using OpenAI's text-davinci-003 model.

    ---

    ### Usage

    1. Select the task you want to perform: either "Update the Database" or "Ask a Question".
    2. Enter the required information: URL for updating the database or a question for semantic search.
    3. Click the "Submit" button.
    4. Wait for the system to update the database or search for the answer.
    5. View the results: the database update success message or the generated answer along with the relevant context.

    ---    
    
    
    """) 