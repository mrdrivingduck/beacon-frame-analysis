"""
    @author mrdrivingduck
    @version 2019-05-05
    @description Learning code of pandaslearning
"""

import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)

s = pd.Series(np.random.randn(5))
print(s)
