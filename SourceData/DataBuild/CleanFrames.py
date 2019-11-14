import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CleanFrame:
    def returnFrame(self):
        return self.frame

    def basicDefine(self):
        frame = self.frame
        print(frame.describe())

class CleanBrowardListings(CleanFrame):
    def __init__(self):
        Listings = pd.read_csv("../BrowardSourceData/listings.csv",
                           dtype={'state': np.str,
                                  'review_scores_rating': np.str,
                                  'review_scores_accuracy': np.str})
        self.SkipRows = [1490, 1879, 1999, 2451, 4840, 5973, 6314, 6329, 6472, 6473, 6519, 6794, 8255, 9075, 10104]
        Listings = Listings.drop(self.SkipRows, axis=0)
        #
        # #loop and remove unnecessary columns
        RemoveColumns = pd.read_csv("../../RemoveColumns.csv")
        for ind in RemoveColumns.index:
            Listings = Listings.drop(RemoveColumns['ColumnName'][ind], axis =1)

        # convert the "price column from strings with $ to numbers"
        Listings['price'] = Listings['price'].replace('[\$,]', '', regex=True).astype(float)

        #Cleanup Complete
        self.frame = Listings

    def ListingDefine(self):
        Listings = self.frame
        print(len(Listings['latitude'].unique())) #output: 7730 unque latitude locations
        print(len(Listings['longitude'].unique())) #output 6720 unique longitude locations

        Listings['price'].plot(kind='box')
        plt.xlabel('prices of Airbnb Broward')
        plt.show()

    def ListingErrors(self):
        Listings = pd.read_csv("../BrowardSourceData/listings.csv")
        #read rows that are causeing type errors
        print(Listings.loc[self.SkipRows, ['state','review_scores_rating', 'review_scores_accuracy']])

        #read file
        Listings = pd.read_csv("../BrowardSourceData/listings.csv")

        #looks for rows where state is not equal to "FL"
        CalObj = Listings.apply(lambda x: False if x['state'] == "FL" or x['state'] == "NaN" else True, axis=1)

        #print sum and list of rows with errors
        numOfTrue = len(CalObj[CalObj == True].index)
        print(numOfTrue)
        print(CalObj[CalObj == True].index)
        # output: [1490,  1879,  1999,  2451,  4840,  5973,  6314,  6329,  6472, 6473,  6519,  6794,  8255,  9075, 10104]


#Calendar and Reviews are here should more in depth analysis is necessary
class CleanBrowardCalendar(CleanFrame):
    def __init__(self):
        calendar = pd.read_csv("../BrowardSourceData/calendar.csv")
        self.frame = calendar


class CleanBrowardReviews(CleanFrame):
    def __init__(self):
        reviews = pd.read_csv("../BrowardSourceData/reviews.csv")
        self.frame = reviews




