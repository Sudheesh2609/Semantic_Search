# Semantic_Search
## Mercor AI Semantic Search Project

This repository contains a Semantic Search Engine built using OpenAI and Pinecone. The search engine allows users to perform semantic search on a database of documents and obtain relevant answers to their questions. The system utilizes sentence embeddings, natural language processing, and machine learning techniques to provide accurate and efficient search results.

## Features

- Update the Database: Users can add new documents to the search index by providing the URL of the document. The system automatically scrapes the text content from the URL, processes it, and adds it to the search index using Pinecone.

- Ask a Question: Users can enter their questions into the system, and it will search the indexed documents to find the most relevant answers using semantic search techniques. The search results include the relevant context from the matching documents and an automatically generated answer using OpenAI's text-davinci-003 model.

## How to Run

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command in jupyter notebook:
```
!pip install sentence_transformers pinecone-client openai -q
```
   OR

   Install the required dependencies by running the following command in command prompt:

```
pip install sentence_transformers pinecone-client openai -q
```
3. These are the required dependencies in this project:

    - openai
    - sentence-transformers
    - pinecone-client
    - BeautifulSoup4
    - streamlit
    
4. Make sure you have the necessary API keys for Pinecone and OpenAI. Update the `vector_search.py` and `qa.py` files with your respective API keys.

5. First run the files: `vector_search.py`, `qa.py` and `utils.py`
6. Run the application `main.py` using the following command: 
```
streamlit run main.py
```
7. Access the streamlit application by opening the provided local URL in your web browser.

## Example

Here's an example of how the Semantic Search Engine works:

1. Choose the task: Update the Database or Ask a Question.
2. If you choose to update the database, enter the URL of the document you want to add.
3. If you choose to ask a question, enter your question in the provided text input.
4. Click the "Submit" button.
5. Wait for the system to update the database or search for the answer.
6. View the results: database update success message or the generated answer along with the relevant context.

## Demo

A hosted version of the Semantic Search Engine is available [here]().

## License

This project is licensed under the [MIT License](LICENSE).



