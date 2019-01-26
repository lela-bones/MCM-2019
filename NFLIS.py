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
    file = open("Report2", "w")
    for substance in substances:
        #saving data to graph
        file.write(substance + "\n")

        for year in years:
            file.write(str(year) + "\n")
            for county in counties:
                #picking the data we need from specific states, counties, drugs, etc.
                dr = np.array(df.loc[(df["FIPS_Combined"] == county) & (df["SubstanceName"] == substance) & (df["YYYY"] == year), "DrugReports"])
                file.write(str(county) + ", Drug Reports = " + str(dr) + "\n")
            file.write("\n")
    file.close()

#This function allows us to look at data for step one
def report1():
    file1 = open("Report1", "w")
    file2 = open("Recovered", "w")
    for year in years:
        file1.write(str(year) + "\n")
        file2.write(str(year) + "\n")
        for county in counties:
            info = np.array(df.loc[(df["FIPS_Combined"] == county) & (df["YYYY"] == year), "TotalDrugReportsCounty"])
            if info.size == 0:
                file2.write(str(county) + ", Drug Reports = 0 \n")
            else:
                file1.write(str(county) + ", Drug Reports = " +  str(info[0]) + "\n")
        file1.write("\n")
        file2.write("\n")
    file1.close()
    file2.close()


#Plotting Arguments
plot_args = [{'c': 'red', 'linestyle': '-'},
             {'c': 'green', 'linestyle': '-'},
             {'c': 'blue', 'linestyle': '-'},
             {'c': 'red', 'linestyle': '--'},
             {'c': 'green', 'linestyle': '--'},
             {'c': 'blue', 'linestyle': '--'},
             {'c': 'black', 'linestyle': '-'},
             {'c': 'black', 'linestyle': '--'}]



report1()
#report2()
