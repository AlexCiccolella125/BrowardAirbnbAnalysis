from SourceData.DataBuild.CleanFrames import CleanBrowardListings
from SourceData.DataBuild.Amenities import clean_amenities
from sklearn.linear_model import LinearRegression
import pandas as pd



gender = pd.read_csv("SourceData/NameSourceData/genderProbability.csv", index_col='name')
for row in gender.iteritems():
    print(row)

# Listings = CleanBrowardListings().returnFrame()
# print(Listings)
# Listings.to_csv(r'Export.csv')