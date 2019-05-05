"""
    @author mrdrivingduck
    @version 2019-05-05
    @description
        To extract features from beacon frames using pyshark
"""

import pyshark
import pandas as pd

frames = pyshark.FileCapture('data/beacon-asusdb202.pcap')
# frames = pyshark.FileCapture('data/beacon-mrdrivingduck.pcap')

rssi_arr = [pkt.radiotap.dbm_antsignal for pkt in frames]
df = pd.DataFrame({"rssi": rssi_arr})
print(df)
df.to_csv('out/rssi.csv')

frames.close()
