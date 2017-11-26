#!/usr/bin/env python

import pandas as pd

# Read in white wine data
white = pd.read_csv("winequality-white.csv", sep=';')

# Read in red wine data
red = pd.read_csv("winequality-red.csv", sep=';')

# Print data information
print(white.info())
print(red.info())

# Print first rows of red
# print(red.head())

# Print last rows of white
# print(white.tail())

# Take a sample of 5 rows of red
# print(red.sample(5))

# Describe white
# print(white.describe())

# Double check for nell values in red
# print(pd.isnull(red))
