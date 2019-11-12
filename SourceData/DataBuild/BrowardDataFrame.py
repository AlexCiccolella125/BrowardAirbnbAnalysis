import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Column AQ,
SkipRows = [1490,  1879,  1999,  2451,  4840,  5973,  6314,  6329,  6472, 6473,  6519,  6794,  8255,  9075, 10104]
Listings = pd.read_csv("../BrowardSourceData/listings.csv",
                       dtype={'state': np.str,
                              'review_scores_rating': np.str,
                              'review_scores_accuracy': np.str})

Listings = Listings.drop(SkipRows, axis=0)

#aadding a comment

#convert the "price column from strings with $ to numbers"
#Listings[Listings.price[1:]].replace('[\$,]', '', regex=True).astype(float)

print(Listings.describe())

# Listings['price'].plot(kind='hist', bins=100)
# plt.xlabel('prices of Airbnb Broward')
# plt.show

"""
#read rows that are causeing type errors
print(Listings.loc[SkipRows, ['state','review_scores_rating', 'review_scores_accuracy']])

#read file
Listings = pd.read_csv("../BrowardSourceData/listings.csv")

#looks for rows where state is not equal to "FL"
CalObj = Listings.apply(lambda x: False if x['state'] == "FL" or x['state'] == "NaN" else True, axis=1)

#print sum and list of rows with errors
numOfTrue = len(CalObj[CalObj == True].index)
print(numOfTrue)
print(CalObj[CalObj == True].index)
# output: [1490,  1879,  1999,  2451,  4840,  5973,  6314,  6329,  6472, 6473,  6519,  6794,  8255,  9075, 10104]
"""