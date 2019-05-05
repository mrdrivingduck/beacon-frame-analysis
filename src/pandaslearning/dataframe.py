"""
    @author mrdrivingduck
    @version 2019-05-05
    @description Learning code ofpandaslearning pandas
"""

import pandas as pd

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])
print(df)

df.to_csv(path_or_buf="out/out.csv")
