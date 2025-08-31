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

The code handles the setup automatically. When you run the first code cell, it will execute the following commands to install the necessary libraries:

`!pip install datasets sentence-transformers chromadb`

***************************************************************************************************************************************************************************************************************************************************************************************************

Usage
To run the project, simply execute all the lines in the script.

1. Run the entire script: Execute all the cells in the script from top to bottom.

2. Observe the Output: The script will provide step-by-step updates on its progress, including data loading, embedding generation, and database population.

3. View Results: After the database is populated, the final cells will perform a semantic search and print the top 5 most relevant documents for the query, demonstrating the core functionality of your vector database.

***************************************************************************************************************************************************************************************************************************************************************************************************

Files

1. vector_database.py: The main script that contains all the logic for data loading, embedding, and searching.

2. vector_database_test.py: A test script I used to query the db

3. vector_database_resukts.py: A file showing the results of my query

4. README.md: A guide on how to utilize this repo

