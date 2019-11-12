from SourceData.DataBuild.CleanFrames import CleanBrowardListings, CleanBrowardCalendar, CleanBrowardReviews
Listings = CleanBrowardListings().returnFrame()
print(Listings)
Calendar = CleanBrowardCalendar().returnFrame()
print(Calendar)
Reviews = CleanBrowardReviews().returnFrame()
print(Reviews)