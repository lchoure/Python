import pandas as pd
import numpy as np
baseball = pd.read_csv("C:\\Users\\A9884\\Python\\Ext_Files\\baseball.csv")[['Height', 'Weight']].to_numpy().tolist()
updated = np.array(pd.read_csv("C:\\Users\\A9884\\Python\\Ext_Files\\update.csv",header = None))
n = len(baseball)

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated

print(np.matrix(np_baseball) + np.matrix(updated))

# Create numpy array: conversion


# Print out product of np_baseball and conversion

