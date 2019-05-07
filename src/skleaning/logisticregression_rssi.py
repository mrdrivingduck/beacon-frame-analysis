"""
    @author mrdrivingduck
    @version 2019-05-07
    @description Use Logistic Regression to predict
"""

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC

import pandas as pd
import matplotlib.pyplot as plt

ap_name = [
    'asc-201',
    'asus-db202',
    'cca01',
    'chaoweilanmao-huawei',
    'chaoweilanmao-soft',
    'dlink',
    'iphonex',
    'mrdk',
    'mrdrivingduck',
    'portal-juniper',
    'portal-trapeze',
    'qwer',
    'surface'
]

target_index = 0

# x -> data
# y -> target(label)
# True class
csv = pd.read_csv(filepath_or_buffer='out/' + ap_name[target_index] + '.csv')
rssi_arr = [[rss] for rss in csv['rssi']]
x = rssi_arr
y = [1 for i in range(len(rssi_arr))]

# False class
for i in range(len(ap_name)):
    if i != target_index:
        csv = pd.read_csv(filepath_or_buffer='out/' + ap_name[i] + '.csv')
        rssi_arr = [[rss] for rss in csv['rssi']]
        for j in range(len(rssi_arr)):
            x.append(rssi_arr[j])
            y.append(0)

# plt.scatter(x, y)
# plt.show()

# Training
# clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(x, y)
# clf = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1).fit(x, y)
# clf = SVC(C=1.0, kernel='rbf', gamma='auto')
clf = GaussianNB().fit(x, y)

# Predict
csv = pd.read_csv(filepath_or_buffer='out/' + ap_name[3] + '.csv')
rssi_arr = [[rss] for rss in csv['rssi']]
test = rssi_arr
res = clf.predict(test)

hit = 0
for i in range(len(res)):
    if res[i] == 0:
        hit = hit + 1

print(hit)
print(len(res))
print(hit / len(res))

# prob = clf.predict_proba(predict)
# print(prob)
# for i in range(len(prob)):
#     if (prob[i][0] <= prob[i][1]):
#         print(prob[i])
#         print(predict[i])
