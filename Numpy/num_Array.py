# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))

np_add_array = np.array([True, 1, 2]) + np.array([3, 4, False])
print('add np array')

print(np_add_array)

baseball = [180, 215, 210, 210, 188, 176, 209, 200]
print(baseball.index(210))