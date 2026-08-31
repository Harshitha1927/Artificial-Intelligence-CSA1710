import numpy as np

# Rows = Users
# Columns = Movies
# 0 means not rated

ratings = np.array([
    [5, 4, 0, 0],
    [5, 0, 4, 0],
    [0, 4, 5, 3],
    [0, 0, 5, 4]
])

print("Rating Matrix:")
print(ratings)

# Calculate similarity
similarity = ratings @ ratings.T

print("\nUser Similarity:")
print(similarity)

# Find most similar user to User 1
user = 0
similar_users = np.argsort(similarity[user])[::-1]

for u in similar_users:
    if u != user:
        break

print("\nMost Similar User:", u + 1)

# Recommend an item
for item in range(ratings.shape[1]):
    if ratings[user][item] == 0 and ratings[u][item] > 0:
        print("Recommended Item:", item + 1)
