import numpy as np
from sklearn.linear_model import LinearRegression

# Training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Get values
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Prediction
x = float(input("Enter X value: "))
prediction = model.predict([[x]])

print("Predicted value:", prediction[0])
