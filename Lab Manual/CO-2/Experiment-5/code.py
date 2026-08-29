from sklearn.tree import DecisionTreeClassifier

X = [[1,0],[1,1],[0,1],[0,0]]
y = [1,1,0,0]

model = DecisionTreeClassifier()
model.fit(X, y)

print(model.predict([[1,0]]))
