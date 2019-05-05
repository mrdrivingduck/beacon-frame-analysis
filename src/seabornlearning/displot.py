"""
    @author mrdrivingduck
    @version 2019-05-05
    @description Learning codes of seaborn
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

rssi_arr = pd.read_csv(filepath_or_buffer="out/rssi.csv")
sns.distplot(rssi_arr["rssi"])
plt.show()
