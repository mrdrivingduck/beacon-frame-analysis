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
    'iphonex'
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
            if len(new_pkt[key]) != len(old_pkt[key]):
                return True
            else:
                for index in range(len(new_pkt[key])):
                    if new_pkt[key][index] != old_pkt[key][index]:
                        return True
        else:
            if new_pkt[key] != old_pkt[key]:
                return True
    return False


ap_pkts_arr = []
for i in range(len(ap_name)):
    frames = pyshark.FileCapture('data/beacon-' + ap_name[i] + '.pcap')
    print('Loading data: ' + ap_name[i])
    pkts = []
    count = 0
    for pkt in frames:
        if count == 0:
            pkts.append(pkt[3].__str__())
        count = count + 1
    ap_pkts_arr.append(pkts)
    frames.close()

for i in range(len(ap_pkts_arr)):
    print('AP - ' + ap_name[i])

    param = None
    comp_param = None

    param = extract_param(ap_pkts_arr[i][0])

    for j in range(len(ap_pkts_arr)):
        if j != i:
            comp_param = extract_param(ap_pkts_arr[j][0])
            print('  [' + ap_name[i] + '] [' + ap_name[j] + '] : ' + str(diff(param, comp_param)))
