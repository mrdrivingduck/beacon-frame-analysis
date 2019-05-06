"""
    @author mrdrivingduck
    @version 2019-05-06
    @description
        To extract features from beacon frames using pyshark
"""

import pyshark
import pandas as pd

# ap_name = 'asusdb202'
ap_name = 'mrdrivingduck'
ap_name = 'surface-soft'
frames = pyshark.FileCapture('data/beacon-' + ap_name + '.pcap')

"""
    @function Extracting RSSI
"""
# rssi_arr = [pkt.radiotap.dbm_antsignal for pkt in frames]
# df = pd.DataFrame({"rssi": rssi_arr})
# print(df)
# df.to_csv('out/' + ap_name + '.csv')

"""
    @function Extracting fixed fields in string format
"""
for pkt in frames:
    print(pkt[3].__str__())
    print(pkt[3].pretty_print())


frames.close()
