from SourceData.DataBuild.CleanFrames import CleanBrowardListings
from SourceData.DataBuild.Amenities import clean_amenities
from sklearn.linear_model import LinearRegression

Listings = CleanBrowardListings().returnFrame()
Listings = clean_amenities(Listings)
print(Listings)
Listings.to_csv(r'../Export.csv')