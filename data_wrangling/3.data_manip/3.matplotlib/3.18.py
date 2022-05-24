import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# genrate random
x = np.random.randint(1,10, 1)
# print(x)
x = np.round(50 + 50 *np.random.random(size=15), 2)
# print(x)

# random numbers between 0 and 1
x = np.random.rand(3,3)
print(x)