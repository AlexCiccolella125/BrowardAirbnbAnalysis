from SourceData.DataBuild.CleanFrames import CleanBrowardListings
from SourceData.DataBuild.Amenities import clean_amenities
from sklearn.linear_model import LinearRegression
import pandas as pd


Listings = CleanBrowardListings().returnFrame()
print(Listings)
Listings.to_csv(r'Export.csv')
