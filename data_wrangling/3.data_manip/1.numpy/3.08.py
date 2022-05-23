import numpy as np


print("Vector of zeros: ",np.zeros(5))
print("Matrix of zeros: \n",np.zeros((3,4), dtype=np.int8))
print("Matrix of 5's: \n",5*np.ones((3,3)))
print("Identity matrix of dimension 2:",np.eye(2))

print(f'Random matrix of shape(4,3):\n{np.random.randint(5, 50, (4,3))}')