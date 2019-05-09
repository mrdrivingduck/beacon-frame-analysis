"""
    @author mrdrivingduck
    @version 2019-05-08
    @description
        To extract features from beacon frames using pyshark
"""

import pyshark
import pandas as pd
from sklearn.preprocessing import StandardScaler

ap_name = [
    'asc-201',
    'mrdrivingduck',
    'bigboy',
    'asus-db202',
    'cca01',
    'dlink',
    'mrdk',
    'portal-juniper',
    'portal-trapeze',
    'qwer',
    'chaoweilanmao-soft',
    'surface',
    'chaoweilanmao-huawei',
    'iphonex',
]


def extract_param(pkt_str):
    pkt_data_arr = pkt_str.split('\r\n\t')
    fingerprint = {
        'Capabilities Information': None,
        'DTIM period': None,
        'Beacon Interval': None,
        'Supported Rates': [],
        'Extended Supported Rates': [],
        'Vendor Specific': [],
        'RSN Capabilities': None
    }
    for index in range(len(pkt_data_arr)):
        if 'Capabilities Information:' in pkt_data_arr[index]:
            fingerprint['Capabilities Information'] = pkt_data_arr[index][len('Capabilities Information:') + 1:]
        if 'DTIM period:' in pkt_data_arr[index]:
            fingerprint['DTIM period'] = pkt_data_arr[index][len('DTIM period:') + 1:]
        if 'Beacon Interval' in pkt_data_arr[index]:
            temp = pkt_data_arr[index].split()
            fingerprint['Beacon Interval'] = temp[2]
        if 'Supported Rates:' in pkt_data_arr[index] and 'Extended Supported Rates:' not in pkt_data_arr[index]:
            temp = pkt_data_arr[index].split()
            fingerprint['Supported Rates'].append(temp[3][1:-1])
        if 'Extended Supported Rates:' in pkt_data_arr[index]:
            temp = pkt_data_arr[index].split()
            fingerprint['Extended Supported Rates'].append(temp[4][1:-1])
        if 'Tag: Vendor Specific:' in pkt_data_arr[index]:
            fingerprint['Vendor Specific'].append(pkt_data_arr[index][len('Tag: Vendor Specific:') + 1:])
        if pkt_data_arr[index].startswith('Capabilities:'):
            fingerprint['RSN Capabilities'] = pkt_data_arr[index][len('Capabilities:') + 1:]

    return fingerprint


def diff(new_pkt, old_pkt):
    for key in new_pkt.keys():
        if isinstance(new_pkt[key], list):
            for index in range(len(new_pkt[key])):
                if new_pkt[key][index] != old_pkt[key][index]:
                    return True
        else:
            if new_pkt[key] != old_pkt[key]:
                return True
    return False


for i in range(len(ap_name)):
    frames = pyshark.FileCapture('data/beacon-' + ap_name[i] + '.pcap')
    print('AP - ' + ap_name[i])

    """
        @function Extracting fixed fields in string format
    """
    param = None
    diff_count = 0
    for pkt in frames:
        new_param = extract_param(pkt[3].__str__())
        if param is None:
            param = new_param
        elif diff(new_param, param):
            param = new_param
            diff_count = diff_count + 1
    print('AP - ' + ap_name[i] + ' diff count: ' + str(diff_count))

    frames.close()
