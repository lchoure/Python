import pandas as pd
baseball = pd.read_csv("C:\\Users\\A9884\\Python\\Ext_Files\\baseball.csv")[['Height', 'Weight']].to_numpy().tolist()

import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123, 0])