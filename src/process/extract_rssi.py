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

for i in range(len(ap_name)):
    frames = pyshark.FileCapture('data/beacon-' + ap_name[i] + '.pcap')
    print('AP - ' + ap_name[i])

    """
        @function Extracting RSSI
    """
    rssi_arr = [pkt.radiotap.dbm_antsignal for pkt in frames]
    ss = StandardScaler()
    origin_data = [[rssi_arr[j]] for j in range(len(rssi_arr))]
    std_data = ss.fit_transform(origin_data)
    print('origin data - ' + str(len(origin_data)))

    std_out = []
    for j in range(len(std_data)):
        if -1 < std_data[j][0] < 1:
            std_out.append(rssi_arr[j])
    print('standard data - ' + str(len(std_out)))

    df = pd.DataFrame({"rssi": std_out})
    if len(df) > 5000:
        df = df.iloc[0:5000, :]

    # print(df)
    # df.to_csv('out/' + ap_name[i] + '.csv')

    """
        @function Extracting fixed fields in string format
    """
    # for pkt in frames:
    #     print(pkt[3].__str__())
    #     print(pkt[3].pretty_print())

    frames.close()
