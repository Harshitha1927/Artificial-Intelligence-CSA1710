from sklearn.svm import SVC

# Training data
X = [
    [1,1],
    [2,2],
    [3,3],
    [7,7],
    [8,8],
    [9,9]
]

y = [0,0,0,1,1,1]

# Create SVM
model = SVC(kernel='linear')

# Train
model.fit(X, y)

# Input
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

# Prediction
result = model.predict([[a,b]])

print("Predicted Class:", result[0])
