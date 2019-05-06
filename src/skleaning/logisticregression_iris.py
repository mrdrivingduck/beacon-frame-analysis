from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

x, y = load_iris(return_X_y=True)
# x -> data
# y -> target(label)
# print(x)
# print(y)
clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(x, y)
res = clf.predict(x)
prob = clf.predict_proba(x)
print(res)
print(prob)
print(y)
