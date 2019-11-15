import pandas
import json
import csv
from notebookAirbnbBostonGender.SourceData.DataBuild.CleanFrames import CleanBrowardListings

Listings = CleanBrowardListings().returnFrame()

def LoopTillComma(row):


def cleanLine(row):
    row.toLower
    for char in row:
        if char == ",":

for index, row in Listings.iterrows():
    AmenitiesArray = str(row['amenities']).strip("{}")
    AmenitiesArray = AmenitiesArray.ToLower()
    for char in AmenitiesArray:

    # data = json.loads(AmenitiesArray)
    # # print(data)
    # for item in AmenitiesArray:
    #     print(item)