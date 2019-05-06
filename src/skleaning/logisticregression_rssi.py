"""
    @author mrdrivingduck
    @version 2019-05-06
    @description Use Logistic Regression to predict
"""

from sklearn.linear_model import LogisticRegression
import pandas as pd

# x -> data
# y -> target(label)
# True class
csv = pd.read_csv(filepath_or_buffer='out/surface-soft.csv')
rssi_arr = [[rss] for rss in csv['rssi']]
x = rssi_arr
y = [1 for i in range(len(rssi_arr))]

# False class
csv = pd.read_csv(filepath_or_buffer='out/mrdrivingduck.csv')
rssi_arr = [[rss] for rss in csv['rssi']]
for i in range(len(rssi_arr)):
    x.append(rssi_arr[i])
    y.append(0)

# Training
clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(x, y)

# Predict
csv = pd.read_csv(filepath_or_buffer='out/asusdb202.csv')
rssi_arr = [[rss] for rss in csv['rssi']]
predict = rssi_arr
res = clf.predict(predict)

hit = 0
for i in range(len(res)):
    if res[i] == 0:
        hit = hit + 1

print(hit)
print(len(res))
print(hit / len(res))

prob = clf.predict_proba(predict)
print(prob)
for i in range(len(prob)):
    if (prob[i][0] <= prob[i][1]):
        print(prob[i])
        print(predict[i])
