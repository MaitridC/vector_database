# -*- coding: utf-8 -*-

# A Vector Database

# Install libraries
!pip install datasets sentence-transformers chromadb

from datasets import load_dataset
from itertools import islice

# Load the SQuAD dataset in streaming mode
# This stops us from loading all the rows on a system with limited memory
print("Loading a subset of the Wikipedia dataset in streaming mode...")
dataset = load_dataset("squad", split="train", streaming=True)


# Process only the first 10000 items from the stream
dataset_slice = islice(dataset, 10000)

# Convert to a list to ensure we have a fixed set of items to work with
dataset_list = list(dataset_slice)
print(f"Loaded {len(dataset_list)} items from the dataset.")

# Example to showcase the data structure
print("\nExample data point and its keys:")
example_item = dataset_list[0]
print(example_item)
print(f"\nAvailable keys in this data point: {list(example_item.keys())}")


# Embed the text data
from sentence_transformers import SentenceTransformer

# Load a pre-trained sentence transformer model
# This transformer will convert text to vectors
print("\nLoading the embedding model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded.")


# Extract the text to embed
documents = [item['context'] for item in dataset_list]

# Remove any duplicate documents to ensure unique results
unique_documents = list(set(documents))
print(f"Removed duplicates. Now working with {len(unique_documents)} unique documents.")


# Generate the embeddings for the documents
print("Generating embeddings for the documents...")
embeddings = model.encode(documents)
print(f"Generated {len(embeddings)} embeddings of dimension {embeddings.shape[1]}.")


# Create the vector database
import chromadb

# Create an in-memory ChromaDB client
print("\nCreating the vector database...")
client = chromadb.Client()

# Collect data into a table to store
collection = client.get_or_create_collection(name="squad_vectors")

# Prepare the data to be added
ids = [f"id_{i}" for i in range(len(documents))]
metadatas = [{"source": "squad"} for _ in range(len(documents))]


# Add the documents and their embeddings
batch_size = 5000
for i in range(0, len(documents), batch_size):
    # Slice the lists to get a smaller chunk
    batch_docs = documents[i:i + batch_size]
    batch_embeddings = embeddings[i:i + batch_size]
    batch_ids = ids[i:i + batch_size]
    batch_metadatas = metadatas[i:i + batch_size]

    # Add the current batch to the table
    collection.add(
        embeddings=batch_embeddings.tolist(),
        documents=batch_docs,
        metadatas=batch_metadatas,
        ids=batch_ids
    )
    print(f"Added batch from index {i} to {i + len(batch_docs)}")

print("All documents and embeddings added to the vector database.")



