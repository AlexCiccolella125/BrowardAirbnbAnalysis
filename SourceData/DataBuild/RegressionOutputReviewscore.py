from SourceData.DataBuild.CleanFrames import CleanBrowardListings, CleanBrowardCalendar, CleanBrowardReviews
Listings = CleanBrowardListings().return_frame()
print(Listings)
Calendar = CleanBrowardCalendar().return_frame()
print(Calendar)
Reviews = CleanBrowardReviews().return_frame()
print(Reviews)