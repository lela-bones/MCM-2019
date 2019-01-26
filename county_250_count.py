import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
#reading in data from NFLIS file
df = pd.read_excel('/Users/caroman/Downloads/2019_MCM-ICM_Problems/2018_MCMProblemC_DATA/MCM_NFLIS_Data.xlsx', sheet_name='Data')


#grabbing the substance unique to each county
counties =  pd.Series(df["FIPS_Combined"]).unique()
substances = pd.Series(df["SubstanceName"]).unique()
years = pd.Series(df["YYYY"]).unique()
states = pd.Series(df["State"]).unique()


#counting how many counties have 250 reported cases and how many counties have more than 250 reported cases
def report():
    total_counties = 461.00
    file1 = open("/Users/caroman/Desktop/Report_lt_250_cases", "w+")
    file2 = open("/Users/caroman/Desktop/Report_mt_250_cases", "w+")
    for year in years:
        count250 = 0
        count251 = 0
        file1.write(str(year) + "\n")
        file2.write(str(year) + "\n")
        for county in counties:
            info = np.array(df.loc[(df["FIPS_Combined"] == county) & (df["YYYY"] == year), "TotalDrugReportsCounty"])

            if info.size == 0 or info[0] <= 250:
                #Drug Reports <= 250
                count250 += 1
            else:
                #Drug Reports > 250 = " +  str(info[0]) + "\n")
                count251 += 1
        
        file1.write(": ")
        file1.write(str(count250))
        file1.write(", ")
        file1.write(str(count250/total_counties))
        file1.write("\n")
        
        file2.write(": ")
        file2.write(str(count251))
        file2.write(", ")
        file2.write(str(count251/total_counties))
        file2.write("\n")
    file1.close()
    file2.close()



report()
