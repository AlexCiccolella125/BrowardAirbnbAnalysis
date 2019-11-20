import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SourceData.DataBuild.Amenities import clean_amenities


class CleanFrame:
    def returnFrame(self):
        return self.frame


class CleanBrowardListings(CleanFrame):
    def __init__(self):
        # reading the listings file
        listings = pd.read_csv("SourceData/BrowardSourceData/listings.csv",
                               # sys:1: DtypeWarning flag is occurring, Columns (43,61,62) have mixed types, dtype is
                               # set to avoid issues.
                               dtype={'state': np.str,
                                      'review_scores_rating': np.str,
                                      'review_scores_accuracy': np.str})

        # The following rows have missing state data and are dropped
        # self.SkipRows = self.listing_errors()
        self.SkipRows = [1490, 1879, 1999, 2451, 4840, 5973, 6314, 6329, 6472, 6473, 6519, 6794, 8255, 9075, 10104]
        listings = listings.drop(self.SkipRows, axis=0)

        # loop and remove unnecessary columns
        remove_columns = pd.read_csv("RemoveColumns.csv")
        for ind in remove_columns.index:
            listings = listings.drop(remove_columns['ColumnName'][ind], axis=1)

        # convert the "price column from strings with $ to numbers"
        listings['price'] = listings['price'].replace('[\$,]', '', regex=True).astype(float)

        # merge the gender data with Listings and with corrected probabilities
        gender = pd.read_csv("SourceData/NameSourceData/genderProbability.csv", index_col='name')
        gender['probability'] = gender.apply(lambda x: x['probability'] if x['gender'] == 'M' else 1 - x['probability'],
                                             axis=1)
        listings = listings.join(gender, on='host_name')

        # replacing all data that is not on the SSA list with 50% probability
        # the two main reason for NaN data are couples who listed both names and corporations that list properties.
        listings.probability = listings.probability.fillna(.5)

        # apply clean amenities
        listings = clean_amenities(listings)

        # Cleanup Complete
        self.frame = listings

    def listing_define(self):  # were made to run tests
        listings = self.frame
        print(len(listings['latitude'].unique()))  # output: 7730 unque latitude locations
        print(len(listings['longitude'].unique()))  # output 6720 unique longitude locations

        listings['price'].plot(kind='box')
        plt.xlabel('prices of Airbnb Broward')
        plt.show()

    def listing_errors(self):  # Made to run tests
        # read rows that are causeing type errors
        print(self.loc[self.SkipRows, ['state', 'review_scores_rating', 'review_scores_accuracy']])

        # looks for rows where state is not equal to "FL"
        cal_obj = self.apply(lambda x: False if x['state'] == "FL" or x['state'] == "NaN" else True, axis=1)

        # print sum and list of rows with errors
        num_of_true = len(cal_obj[cal_obj].index)
        print(num_of_true)
        return cal_obj[cal_obj == True].index
        # output: [1490, 1879, 1999, 2451, 4840, 5973, 6314, 6329, 6472, 6473, 6519, 6794, 8255, 9075, 10104]


# Calendar and Reviews are here should more in depth analysis is necessary
class CleanBrowardCalendar(CleanFrame):
    def __init__(self):
        calendar = pd.read_csv("SourceData/BrowardSourceData/calendar.csv")
        self.frame = calendar


class CleanBrowardReviews(CleanFrame):
    def __init__(self):
        reviews = pd.read_csv("SourceData/BrowardSourceData/reviews.csv")
        self.frame = reviews
