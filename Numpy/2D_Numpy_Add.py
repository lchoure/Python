import pandas as pd
import numpy as np
baseball = pd.read_csv("read_CSV")[['Height', 'Weight']].to_numpy().tolist()
updated = np.array(pd.read_csv("Read CSV update",header = None))
n = len(baseball)

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated

print(np.matrix(np_baseball) + np.matrix(updated))

# Create numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(np_baseball * conversion)

