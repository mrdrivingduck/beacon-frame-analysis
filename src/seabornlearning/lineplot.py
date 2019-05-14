"""
    @author mrdrivingduck
    @version 2019-05-14
    @description Learning codes of seaborn
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="darkgrid")

df = pd.read_csv(filepath_or_buffer='data/accuracy.csv')
print(df)

sns.lineplot(x="AP", y="Accuracy",
             hue="Algorithm",
             data=df)

plt.ylim(0.6, 1.05)
# plt.show()
plt.savefig('out/accuracy.pdf', format='pdf')
