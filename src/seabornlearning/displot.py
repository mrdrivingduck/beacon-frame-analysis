"""
    @author mrdrivingduck
    @version 2019-05-07
    @description Learning codes of seaborn
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

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

for i in range(len(ap_name)):
    rssi_arr = pd.read_csv(filepath_or_buffer="out/" + ap_name[i] + ".csv")

    sns.distplot(rssi_arr["rssi"], norm_hist=True)
    plt.show()
