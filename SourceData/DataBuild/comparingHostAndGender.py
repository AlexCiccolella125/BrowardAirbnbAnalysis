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

#print(Listings[~Listings.host_name.isin(nameGender.name)].host_name)
#returns a list of names not in the table (3583 thousand)
#print(Listings[Listings.host_name.isin(nameGender.name)].host_name)

print(sum(1 for row in Listings['host_id'].unique()))


"""types of analysis {
    linear regression
    logistic regression
    k-nearest neighbors
    neural networks
    classification and regression trees
    cluster analysis
}"""










"""

Message for Gaby***
Hello mayor Hunschofsky,

It was a pleasure speaking with you at the Isreal Dinner at FAU. 
Your work with the students of parkland is inspiring. 
Given my past experience with gun violence as a child, 
I have always been motivated to take action and help others who have become victims as well.
My ultimate goal is to become a LMHC specialised in PTSD and trauma.

Following up with out conversation, you had mentioned that you would be able to help me get in contact with trauma 
specialists in Broward county. I really hope to use my skills as a psychology major to make a difference.

Thank you again for all your time and help you give to our community,
Gabriella Pettit.

"""