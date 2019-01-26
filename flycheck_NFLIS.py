import pandas as pd
import numpy as np
#  reading in data from NFLIS file
df = pd.read_excel('Data/MCM_NFLIS_Data.xlsx', sheet_name='Data')
#  print(data)

#grabbing the substance unique to each county
counties =  pd.Series(df["COUNTY"]).unique()
substances = pd.Series(df["SubstanceName"]).unique()
years = pd.Series(df["YYYY"]).unique()
states = pd.Series(df["State"]).unique()

for substance in substances:
    #saving data to graph
    data = []
    print(substance)
    for year in years:
        print(year)
        for state in states:
            for county in counties:
                #picking the data we need from specific states, counties, drugs, etc.
                dr = np.array(df.loc[(df["State"] == state) & (df["COUNTY"] == county) & (df["SubstanceName"] == substance) & (df["YYYY"] == year), "DrugReports"])
                print(county, ", Drug Reports = ", dr)
                #a
                data.append(dr)
