SQuAD Vector Database Project

This project demonstrates a simple but powerful application of a vector database for semantic search. 
The system uses a subset of the SQuAD (Stanford Question Answering Dataset) and a pre-trained model to create a vector-based index, allowing for highly relevant search results based on the meaning of the text, not just keywords.

***************************************************************************************************************************************************************************************************************************************************************************************************

Features

1. Data Loading: Loads a text-based dataset directly from the Hugging Face Hub using a streaming approach to conserve memory.

2. Data Deduplication: Removes duplicate documents to ensure unique and meaningful search results.

3. Vectorization: Utilizes a Sentence-Transformers model to convert text into numerical vectors (embeddings).

4. Vector Database: Uses ChromaDB, a lightweight, open-source vector database, to store and index the embeddings.

5. Semantic Search: Performs a similarity search to find the most relevant documents based on a query's meaning.

***************************************************************************************************************************************************************************************************************************************************************************************************

How It Works

The core idea is to move beyond keyword matching. The system transforms all documents and user queries into high-dimensional vectors. It then finds the documents with vectors that are most "similar" to the query vector, using a distance metric like cosine similarity. This means a search for "Who invented the telephone?" can find a paragraph that mentions "Alexander Graham Bell" even if the query text doesn't contain that name.

***************************************************************************************************************************************************************************************************************************************************************************************************

Setup and Installation

Prerequisites
A Google Colab notebook or a Python environment with the required packages.

Installation
Open this script in your local or a notebook.

The first cell of the script will automatically install all the required Python packages (datasets, sentence-transformers, chromadb).

Usage
To run the project, simply execute all the cells in the notebook.

The script will:

Load the SQuAD dataset.

Filter for unique documents.

Load the embedding model.

Generate embeddings and populate the ChromaDB vector database in batches.

Perform a sample search for "Who invented the telephone?" and print the top results to the console.

Files
vector_database.py: The main script that contains all the logic for data loading, embedding, and searching.

vector_database_test.py: A test script I used to query the db

vector_database_resukts.py: A file showing the results of my query

