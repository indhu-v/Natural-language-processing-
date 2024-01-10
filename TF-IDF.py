from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample document collection
documents = [
    "TF-IDF, or term frequency-inverse document frequency, is a statistic that evaluates the importance of a word in a document relative to a collection of documents.",
    "It is often used in information retrieval and text mining.",
    "The TF-IDF score increases with the frequency of the word in the document and is offset by the frequency of the word in the entire collection of documents.",
    "In other words, TF-IDF highlights words that are unique to a document and are not common across many documents.",
    "To implement TF-IDF, you need to calculate the term frequency and inverse document frequency for each word in the document collection.",
]

# Query
query = "TF-IDF in information retrieval"

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + [query])

# Calculate cosine similarity between the query and each document
cosine_similarities = linear_kernel(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

# Rank documents based on cosine similarities
document_ranking = sorted(enumerate(cosine_similarities), key=lambda x: x[1], reverse=True)

# Display the ranked documents
print("Ranked Documents:")
for idx, similarity in document_ranking:
    print(f"Document {idx + 1}: Similarity = {similarity:.4f}")
    print(f"   {documents[idx]}")
    print()
