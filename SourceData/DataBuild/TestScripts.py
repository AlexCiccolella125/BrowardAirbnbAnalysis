from notebookAirbnbBostonGender.SourceData.DataBuild.CleanFrames import CleanBrowardListings
from sklearn.linear_model import LinearRegression

Listings = CleanBrowardListings().returnFrame()
# print(Listings)
Listings.to_csv(r'../Export.csv')
'''
mlr = LinearRegression().fit(Listings[["latitude",
                  "longitude",
                  "accommodates",
                  "bathrooms",
                  "bedrooms",
                  "beds",
                  "calculated_host_listings_count",
                  "cleaning_fee",
                  "extra_people",
                  "guests_included",
                  "has_availability",
                  "host_acceptance_rate",
                  "host_has_profile_pic",
                  "host_identity_verified",
                  "host_is_superhost",
                  "host_listings_count",
                  "host_response_rate",
                  "host_response_time",
                  "host_since",
                  "host_total_listings_count",
                  "host_verifications",
                  "house_rules",
                  "id",
                  "instant_bookable",
                  "is_location_exact",
                  "last_review",
                  "maximum_maximum_nights",
                  "maximum_minimum_nights",
                  "maximum_nights",
                  "maximum_nights_avg_ntm",
                  "minimum_maximum_nights",
                  "minimum_minimum_nights",
                  "minimum_nights",
                  "minimum_nights_avg_ntm",
                  "monthly_price",
                  "neighbourhood_cleansed",
                  "neighbourhood_group_cleansed",
                  "number_of_reviews",
                  "number_of_reviews_ltm",
                  "property_type",
                  "require_guest_phone_verification",
                  "reviews_per_month",
                  "room_type",
                  "security_deposit",
                  "square_feet"]], Listings['price'])

print(mlr.intercept__)
print(mlr.coef__)
'''