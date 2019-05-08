"""
    @author mrdrivingduck
    @version 2019-05-08
    @description Running machine learning algorithm and printing results.
"""

import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC

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
    'surface',
    'bigboy'
]


def run(running_index):

    training_df = pd.read_csv(filepath_or_buffer="training/" + ap_name[running_index] + ".csv")
    training_feature = training_df['feature']
    training_label = training_df['label']

    testing_df = pd.read_csv(filepath_or_buffer="testing/" + ap_name[running_index] + ".csv")
    testing_feature = testing_df['feature']
    testing_label = testing_df['label']

    training_data = [[training_feature[i]] for i in range(len(training_feature))]
    testing_data = [[testing_feature[i]] for i in range(len(testing_feature))]

    print('------ Training ------')
    clf_log_reg = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial')\
        .fit(training_data, training_label)
    clf_lin_reg = LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=1)\
        .fit(training_data, training_label)
    clf_svm = SVC(C=1.0, kernel='rbf', gamma='auto')\
        .fit(training_data, training_label)
    clf_gau_nb = GaussianNB()\
        .fit(training_data, training_label)
    clf_mul_nb = MultinomialNB()\
        .fit(training_data, training_label)
    clf_ber_nb = BernoulliNB()\
        .fit(training_data, training_label)

    clf_arr = [
        ['Logistic Regression', clf_log_reg],
        ['Linear Regression', clf_lin_reg],
        ['SVM', clf_svm],
        ['Gaussian Naive Bayes', clf_gau_nb],
        ['polynomial Naive Bayes', clf_mul_nb],
        ['Bernoulli Naive Bayes', clf_ber_nb]
    ]

    print('------ Testing ------')
    for i in range(len(clf_arr)):
        res = clf_arr[i][1].predict(testing_data)
        correct = 0
        for j in range(len(res)):
            if res[j] == testing_label[j]:
                correct = correct + 1
        print(clf_arr[i][0] + ':')
        print('Classification: ' + str(correct) + ' / ' + str(len(res)))
        print('Accuracy: ' + str(correct / len(res)))
        print('------')


run(13)
