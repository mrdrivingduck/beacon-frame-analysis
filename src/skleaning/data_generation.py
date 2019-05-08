"""
    @author mrdrivingduck
    @version 2019-05-08
    @description Calculate the distance of
"""

import pandas as pd
import random as rd
import numpy as np

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


def sequence_gen(arr, seq_len):
    seq = []
    for count in range(seq_len):
        rand = rd.randint(0, len(arr) - 1)
        seq.append(arr[rand])
    return seq


def export_to_file(file_path, feature, label):
    df = pd.DataFrame({
        'feature': [feature[_i][0] for _i in range(len(feature))],
        'label': label
    })
    df.to_csv(file_path)


def data_generation(ap_index, iteration, sample_len):
    feature_arr = []
    label_arr = []

    for i in range(iteration):
        rssi_arr = pd.read_csv(filepath_or_buffer="out/" + ap_name[ap_index] + ".csv")['rssi']
        A = sequence_gen(rssi_arr, sample_len)
    
        A_array = []
        B_array = []
        for j in range(len(ap_name)):
            if j != ap_index:
                other_rssi_arr = pd.read_csv(filepath_or_buffer="out/" + ap_name[j] + ".csv")['rssi']
                _A = sequence_gen(rssi_arr, sample_len)
                B = sequence_gen(other_rssi_arr, sample_len)
                A_array.append(_A)
                B_array.append(B)
    
        for j in range(len(A_array)):
            v1 = np.array(A)
            v2 = np.array(A_array[j])
            v3 = np.array(B_array[j])
            dist_true = np.linalg.norm(v1-v2)
            dist_false = np.linalg.norm(v1-v3)
            feature_arr.append([dist_true])
            label_arr.append(1)
            feature_arr.append([dist_false])
            label_arr.append(0)
    
    print('------ Training Set ------')
    print(len(feature_arr))
    
    predict_arr = []
    reality_arr = []
    for i in range(int(len(feature_arr) / 10 / (len(ap_name) - 1) / 2)):
        A = sequence_gen(rssi_arr, sample_len)
        A_array = []
        B_array = []
        for j in range(len(ap_name)):
            if j != ap_index:
                other_rssi_arr = pd.read_csv(filepath_or_buffer="out/" + ap_name[j] + ".csv")['rssi']
                _A = sequence_gen(rssi_arr, sample_len)
                B = sequence_gen(other_rssi_arr, sample_len)
                A_array.append(_A)
                B_array.append(B)
        for j in range(len(A_array)):
            v1 = np.array(A)
            v2 = np.array(A_array[j])
            v3 = np.array(B_array[j])
            dist_true = np.linalg.norm(v1-v2)
            dist_false = np.linalg.norm(v1-v3)
            predict_arr.append([dist_true])
            reality_arr.append(1)
            predict_arr.append([dist_false])
            reality_arr.append(0)
    
    print('------ Testing Set ------')
    print(len(predict_arr))

    export_to_file('training/' + ap_name[ap_index] + '.csv', feature_arr, label_arr)
    export_to_file('testing/' + ap_name[ap_index] + '.csv', predict_arr, reality_arr)


data_generation(12, 500, 100)
