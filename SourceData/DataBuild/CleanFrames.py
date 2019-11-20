import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SourceData.DataBuild.Amenities import clean_amenities, convert_boolean


class CleanFrame:
    def return_frame(self):
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

        # convert T or F into Binary 1 and 0 respectively
        listings = convert_boolean(listings, ["host_is_superhost", "host_has_profile_pic", "host_identity_verified"])

        # add 0 to empty rows
        for column in ["security_deposit", "cleaning_fee", "host_response_rate"]:
            listings[column].fillna(0, inplace=True)

        # remove $ from monetary values
        for column in ["security_deposit", "cleaning_fee", "extra_people"]:
            listings[column] = listings[column].replace('[\$,]', '', regex=True).astype(float)

        # remove % from host_response_rate
        listings['host_response_rate'] = listings['host_response_rate'].replace('[\%]', '', regex=True).astype(float)

        # make dummmy variables from room_type, property type, bed_type, city
        for column in ["room_type", "property_type", "bed_type", "city"]:
            dummmyframe = pd.get_dummies(listings[column].str.lower())
            listings = listings.join(dummmyframe, rsuffix='_dummy')

        # read gender csv
        gender = pd.read_csv("SourceData/NameSourceData/genderProbability.csv", index_col='name')
        # merge the gender data with corrected probabilities and Listings
        gender['probability'] = gender.apply(lambda x: x['probability'] if x['gender'] == 'M' else 1 - x['probability'],
                                             axis=1)
        listings = listings.join(gender, on='host_name')

        # replacing all data that is not on the SSA list with 50% probability
        # the two main reason for NaN data are couples who listed both names and corporations that list properties.
        listings.probability = listings.probability.fillna(.5)

        # apply clean amenities
        listings = clean_amenities(listings)

        # drop all rows & columns with missing data
        listings.dropna(axis=1, inplace=True)
        listings.dropna(axis=0, inplace=True)

        # Cleanup Complete
        self.frame = listings

    def listing_define(self):  # were made for discovery and testing
        listings = self.frame
        print(len(listings['latitude'].unique()))  # output: 7730 unque latitude locations
        print(len(listings['longitude'].unique()))  # output 6720 unique longitude locations

        listings['price'].plot(kind='box')
        plt.xlabel('prices of Airbnb Broward')
        plt.show()

    def list_type_errors(self):  # were made for discovery and testing
        # looks for rows where state is not equal to "FL"
        cal_obj = self.apply(lambda x: False if x['state'] == "FL" or x['state'] == "NaN" else True, axis=1)

        # print sum and list of rows with errors
        num_of_true = len(cal_obj[cal_obj].index)
        print(num_of_true)
        return cal_obj[cal_obj == True].index
        # output: [1490, 1879, 1999, 2451, 4840, 5973, 6314, 6329, 6472, 6473, 6519, 6794, 8255, 9075, 10104]