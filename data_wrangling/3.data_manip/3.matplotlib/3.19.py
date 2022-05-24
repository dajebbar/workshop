import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


x = np.random.binomial(10, 0.6, 8)
# print(x)

plt.figure(figsize=(7,4))
plt.title('Number of successes in coin toss', fontsize=16)
plt.bar(x=np.arange(1, 9), height=x)
plt.xlabel('Experiment number', fontsize=16)
plt.ylabel('Number of succes', fontsize=16)

plt.show()