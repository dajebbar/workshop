from cProfile import label
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# x = np.random.normal()
# print(x)

student_heights = np.random.normal(loc=155, scale=10, size=100)

# plotting
plt.figure(figsize=(12,8))
plt.title('Young Students height', fontsize=16)
plt.hist(x=student_heights, color='k')
plt.xlabel('heights(cm)', fontsize=16)
plt.ylabel('freq', fontsize=16)

plt.show()