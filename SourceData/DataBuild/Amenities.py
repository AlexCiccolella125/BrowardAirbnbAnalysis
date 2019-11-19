import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from pandas import Series


def clean_amenities(df):
    # removes quotes and creates the list
    def clean_line(datarow):
        datarow = datarow.replace('"', '')
        item_list = datarow.split(",")
        return item_list

    # declaring empty variables

    amenities_array = []
    amenities_dict = {}

    # calling Clean_line to populate the lists with manipulable amenities data
    for index, row in df.iterrows():
        list_amen_row = clean_line(str(row['amenities']).strip("{}"))
        amenities_array.append(list_amen_row)
        amenities_dict[row["host_id"]] = list_amen_row

    # returns the host_id and an array of amenities
    # for row in amenities_dict.items():
    #     print(row)

    # count occurrences of amenity in data and add to dictionary
    amendict = {}
    for spool in amenities_array:
        for item in spool:
            if item in amendict:
                amendict[item] += 1
            else:
                amendict[item] = 1

    # print(amenities_dict.items())
    # print(pd.DataFrame(amenities_dict.items(), columns=("host_id", "amenities_array")))
    # print(pd.DataFrame(dict([(k, Series(v)) for k, v in amenities_dict.items()])))
    # dummyframe = pd.get_dummies(pd.DataFrame.from_dict(amenities_dict, orient='index'))
    # print(dummyframe)
    amenities_dict = pd.Series(amenities_dict)
    dummyframe = pd.get_dummies(amenities_dict.apply(pd.Series).stack()).sum(level=0)
    df = df.join(dummyframe, on='host_id')
    return df

    # print(sorted(((value, key) for (key, value) in amendict.items()), reverse=True))
    # print(len(amendict))
    # mean = statistics.mean(amendict.values())
    # stdev = statistics.stdev(amendict.values())
    # median = statistics.median(amendict.values())
    # print(mean - 3 * stdev)
    # plt.boxplot(amendict.values())
    # plt.show()
