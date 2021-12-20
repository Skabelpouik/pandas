# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 10:07:33 2021

@author: Peridot
"""

import pandas as pd

# Use the tsv file and assign it to a dataframe called food
food = pd.read_csv("Documents\Simplon\Rendu\semaine131221\Pandas\en.openfoodfacts.org.products.tsv", sep="\t")
# See the first 5 entries
print(food.head())
# Print the number of observations in the dataset?
print("Row count is: %s" % food.shape[0])
# Print the number of columns in the dataset
print("Columns count is: %s" % food.shape[1])
# Print the name of all column
print("Name of all columns: %s", food.keys())
# Print the name of 105th column
print("The name of 105th column is: %s" % food.columns[104])
# Print the type of the observations of the 105th column
print("The type of the observations of 105th column is: %s" % food.dtypes[104])
# Print the dataset indexed
print(food.index)
# Print the product name of the 19th observation
print("The product name of the 19th observation is: %s" % food["product_name"][18])