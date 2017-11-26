#!/usr/bin/env python

import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd
import numpy as np
import seaborn as sns
# Import `train_test_split` from `sklearn.model_selection`
from sklearn.model_selection import train_test_split

# Read in white wine data
white = pd.read_csv("winequality-white.csv", sep=';')

# Read in red wine data
red = pd.read_csv("winequality-red.csv", sep=';')

# Add `type` column to `red` with value 1
red['type'] = 1

# Add `type` column to `white` with value 0
white['type'] = 0

# Append `white` to `red`
wines = red.append(white, ignore_index=True)

# Specify the data
X = wines.ix[:, 0:11]

# Specify the target labels and flatten the array
y = np.ravel(wines.type)

# Split the data up in train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
