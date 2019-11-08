import csv
import pandas as pd

"""
with open("../NameGenderProb/name_gender.csv", newline='') as csvfile:
    nameGender = csv.reader(csvfile)
    #print(sum(1 for row in nameGender)) #returns 95027, the count of names in file
    for row in nameGender:
"""

nameGender = pd.read_csv("../NameGenderProb/name_gender.csv")
Listings = pd.read_csv("../bostonAirbnb/listings.csv")

print(Listings[~Listings.host_name.isin(nameGender.name)].host_name)
#returns a list of names not in the table (3583 thousand)
#print(Listings[Listings.host_name.isin(nameGender.name)].host_name)

#print(sum(1 for row in Listings['host_id'].unique()))
