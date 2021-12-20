# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:41:42 2021

@author: Peridot
"""
# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo.
chipo = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv", sep="\t")
# Step 4. See the first 10 entries
print(chipo.head(10))
# Step 5. What is the number of observations in the dataset?
print("Row count is: %s" % chipo.shape[0])
print("Row count is: %s" % len(chipo.index))
# Step 6. What is the number of columns in the dataset?
print("Number of columns in the dataset is: %s" % len(chipo.columns))
# Step 7. Print the name of all the columns.
print("Name of all columns: %s" % chipo.keys())
# Step 8. How is the dataset indexed?
print(chipo.index)
# Step 9. Which was the most-ordered item?
item = chipo.groupby(by="item_name").sum().sort_values("quantity",ascending=False).head(1)
print("The most ordered item is: %s" % item.index[0])
# Step 10. For the most-ordered item, how many items were ordered?
print("%s items were ordered" % item['quantity'][0])
# Step 11. What was the most ordered item in the choice_description column?
items = chipo[['choice_description','quantity']].groupby('choice_description').agg(['count','sum']).sort_values(('quantity', 'sum'), ascending=False)
print(items.index[0])
# Step 12. How many items were orderd in total?
print(chipo['quantity'].sum())
# Step 13. Turn the item price into a float
# Step 13.a. Check the item price type
print(chipo.dtypes["item_price"])
# Step 13.b. Create a lambda function and change the type of item price
chipo["item_price"] = chipo["item_price"].str.replace("$","").astype(float)
# Step 13.c. Check the item price type
print(chipo.dtypes["item_price"])
# Step 14. How much was the revenue for the period in the dataset?
total_revenue = (chipo["quantity"] * chipo["item_price"]).sum()
print("The revenue for the period in the dataset is %s" % total_revenue)
# Step 15. How many orders were made in the period?
print("%d orders were made in the period." % chipo['order_id'].nunique())
# Step 16. What is the average revenue amount per order?
print(chipo.groupby(by=['order_id']).sum().mean()['item_price'])
# Step 17. How many different items are sold?
print("There are %d different items are sold." % chipo['item_name'].nunique())