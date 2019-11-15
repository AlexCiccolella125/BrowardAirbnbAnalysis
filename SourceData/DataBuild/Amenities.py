import pandas
import json
import csv
from SourceData.DataBuild.CleanFrames import CleanBrowardListings

def clean_amenities(df):
    def loop_till_comma(row):
        item_list = row.split(",")
        return item_list

    def clean_line(row):

        return loop_till_comma(row.replace('"',''))

    amenities_array = []
    for index, row in df.iterrows():
        amenities_array.append(clean_line(str(row['amenities']).strip("{}")))

    for spool in amenities_array:
        print(spool)



listings = CleanBrowardListings().returnFrame()
clean_amenities(listings)