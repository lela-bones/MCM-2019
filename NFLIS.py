import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  reading in data from NFLIS file
df = pd.read_excel('Data/MCM_NFLIS_Data.xlsx', sheet_name='Data')
#  print(data)

#grabbing the substance unique to each county
counties =  pd.Series(df["FIPS_Combined"]).unique()
substances = pd.Series(df["SubstanceName"]).unique()
years = pd.Series(df["YYYY"]).unique()
states = pd.Series(df["State"]).unique()


# This function prints the county, year and amount of reports
def report2():
    for substance in substances:
        #saving data to graph
        print(substance)

        for year in years:
            print(year)
            for county in counties:
                #picking the data we need from specific states, counties, drugs, etc.
                dr = np.array(df.loc[(df["FIPS_Combined"] == county) & (df["SubstanceName"] == substance) & (df["YYYY"] == year), "DrugReports"])
                print(county, ", Drug Reports = ", dr)
            print()

#This function allows us to look at data for step one
def report1():
    for year in years:
        for county in counties:
            info = np.array(df.loc[(df["FIPS_Combined"] == county) & (df["YYYY"] == year), "TotalDrugReportsCounty"])
        print(county, ", Drug Reports = ", info)



report1()
report2()
