import pandas as pd


# Calendar = pd.read_csv("AirbnbData/bostonAirbnb/calendar.csv")
# print(Calendar.listing_id.unique())

#I am looking for the average number of days a listing is available for

#number of items in index = 1308890
#print(len(Calendar.index))


# CalObj = Calendar.apply(lambda x: True if x['listing_id'] != 365 else False, axis=1)
# #count number of true in series
# numOfTrue = len(CalObj[CalObj == True].index)
#
# print(numOfTrue)
#
# CalOBJ = Calendar.groupby('listing_id').count()
# Calendar_not_365 = CalOBJ[CalOBJ.date > 365]
# print(Calendar_not_365)

# print(Calendar[Calendar.listing_id.unique < 365])

#
# Calendar_not_365 = Calendar[Calendar.listing_id == 12898806]
# print(Calendar_not_365)


"""      state review_scores_rating review_scores_accuracy
1490     FL                   95                      9
1879     FL                   90                      9
1999     FL                   95                     10
2451     FL                   96                     10
4840     FL                  100                     10
5973     FL                  NaN                    NaN
6314     FL                  100                     10
6329     FL                  100                     10
6472     FL                  100                     10
6473     FL                  100                     10
6519     FL                   95                      9
6794     FL                   73                      9
8255     FL                  NaN                    NaN
9075     FL                   60                     10
10104    FL                  NaN                    NaN"""