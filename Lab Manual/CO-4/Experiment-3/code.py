from sklearn.neighbors import KNeighborsClassifier

# Training data
X = [[1,1], [2,2], [3,3], [6,6], [7,7]]
y = ['A', 'A', 'A', 'B', 'B']

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X, y)

# Input
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

# Prediction
result = model.predict([[a,b]])

print("Predicted Class:", result[0])
