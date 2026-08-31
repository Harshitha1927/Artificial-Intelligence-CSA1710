from sklearn.tree import DecisionTreeClassifier

# Training data
X = [
    [1,0],
    [1,1],
    [0,1],
    [0,0],
    [1,0],
    [0,1]
]

y = [1,1,0,0,1,0]

# Create Decision Tree
model = DecisionTreeClassifier()

# Train
model.fit(X, y)

# Get input
a = int(input("Enter first value (0/1): "))
b = int(input("Enter second value (0/1): "))

# Predict
result = model.predict([[a,b]])

print("Predicted Class:", result[0])
