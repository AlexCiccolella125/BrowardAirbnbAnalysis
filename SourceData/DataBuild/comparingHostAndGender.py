from SourceData.DataBuild.CleanFrames import CleanBrowardListings
import pandas as pd
import numpy as np
import sklearn.linear_model as LinearRegression

nameGender = pd.read_csv("../NameGenderProb/name_gender.csv")
Listings = CleanBrowardListings().returnFrame()

#returns a list of names not in the table (2669 thousand)
print(Listings[~Listings.host_name.isin(nameGender.name)].host_name)

#returns name IN both tables (7545 thousand)
print(Listings[Listings.host_name.isin(nameGender.name)].host_name)

print("NOT in SSA list: ", sum(1 for row in Listings[~Listings.host_name.isin(nameGender.name)].host_name))
print("Names in SSA list: ", sum(1 for row in Listings[Listings.host_name.isin(nameGender.name)].host_name))
print("Unique names: ", sum(1 for row in Listings['host_id'].unique()))


"""types of analysis {
    linear regression
    logistic regression
    k-nearest neighbors
    neural networks
    classification and regression trees
    cluster analysis
}"""
