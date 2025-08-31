# TESTING: LET'S QUERY OUR DB!

# What is the size of our DB?
print(f"Database collection '{collection.name}' contains {collection.count()} items.")

# Define the query text
query_text = "What is University of Notre Dam known for?"

# Embed the query text using the same model
print(f"\nEmbedding the query text: '{query_text}'")
query_embedding = model.encode([query_text]).tolist()

# Query the DB for the top 2 most similar results
print("Querying the database for similar documents...")
results = collection.query(
    query_embeddings=query_embedding,
    n_results=2
)

# Print the results
print("\n--- Query Results ---")
for i, (doc, dist) in enumerate(zip(results['documents'][0], results['distances'][0])):
    if i >= 2:
          break
    print(f"Result {i+1}: (Distance: {dist:.4f})")
    print(f"Document: {doc}...")
    print("-" * 20)
