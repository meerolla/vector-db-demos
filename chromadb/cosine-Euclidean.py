import numpy as np
from numpy.linalg import norm

a = np.array([1, 2])
b = np.array([2, 3])

# Cosine similarity
cos_sim = np.dot(a, b) / (norm(a) * norm(b))

# Euclidean distance
euclidean = norm(a - b)

print(f"Cosine similarity: {cos_sim:.4f}")
print(f"Euclidean distance: {euclidean:.4f}")
