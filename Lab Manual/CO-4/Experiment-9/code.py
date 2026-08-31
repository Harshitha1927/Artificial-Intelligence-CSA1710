import numpy as np
from sklearn.decomposition import PCA

# Dataset
X = np.array([
    [2,4],
    [3,6],
    [4,8],
    [5,10]
])

print("Original Data:")
print(X)

# Create PCA
pca = PCA(n_components=1)

# Reduce dimensions
result = pca.fit_transform(X)

print("\nReduced Data:")
print(result)

print("\nExplained Variance:")
print(pca.explained_variance_ratio_)
