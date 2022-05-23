import pandas as pd
import numpy as np

df = pd.DataFrame(
    data=np.random.randint(-10,100,100).reshape(10,10),
    columns=[f'f_{x}' for x in range(1, 11)]
)
print(df.sample(8))