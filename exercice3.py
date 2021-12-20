# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:12:29 2021

@author: Peridot
"""

# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from this address.
# Step 3. Assign it to a variable called chipo.
euro12 = pd.read_csv("Documents\Simplon\Rendu\semaine131221\Pandas\Euro_2012_stats_TEAM.csv", sep=",")
# Step 4. Select only the Goal column.
print(euro12['Goals'])
# Step 5. How many team participated in the Euro2012?
print(euro12['Team'].count())
# Step 6. What is the number of columns in the dataset?
print(euro12.shape[1])
# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)
# Sort the teams by Red Cards, then to Yellow Cards
discipline = discipline.sort_values(by=['Red Cards','Yellow Cards'], ascending=False)
print(discipline)
# Step 9. Calculate the mean Yellow Cards given per Team
print(discipline["Yellow Cards"].mean())
# Step 10. Filter teams that scored more than 6 goals
more_than_6 = euro12.query("Goals > 6")
print(more_than_6)
# Step 11. Select the teams that start with G
# Step 12. Select the first 7 columns
# Step 13. Select all columns except the last 3.
# Step 14. Present only the Shooting Accuracy from England, Italy and Russia