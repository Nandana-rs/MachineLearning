from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
from sklearn import tree
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
predi = DecisionTreeClassifier()
predi.fit(X_train, y_train)
y_pred = predi.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print(classification_report(y_test, y_pred))
print(f'Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}')
plt.figure(figsize=(10, 5))
tree.plot_tree(predi, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)

plt.show()