"""
    @author mrdrivingduck
    @version 2019-05-06
    @description Use Logistic Regression to predict
"""

from sklearn.linear_model import LogisticRegression
import pandas as pd

# x -> data
# y -> target(label)
x = pd.read_csv(filepath_or_buffer='out/rssi.csv')
x = [[rss] for rss in x['rssi']]
y = [1 for i in range(len(x))]

# Training
clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial').fit(x, y)
