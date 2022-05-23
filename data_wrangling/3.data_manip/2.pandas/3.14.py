import pandas as pd
import numpy as np


df = pd.DataFrame(
    data=np.random.randint(1,10,20).reshape(5,4),
    index=list('ABCDE'),
    columns=list('WXYZ')
)
print(df)

d={'a':[10,20],'b':[30,40],'c':[50,60]}
df = pd.DataFrame(data=d, index=list('XY'))
print(df)