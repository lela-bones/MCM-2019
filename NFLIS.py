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


#Report1, but broken down by states
def report3():
    file = open("Report3", "w")
    sums = 0
    for state in states:
        data = df.loc[df["State"]== state]
        data = pd.Series(data["FIPS_Combined"]).unique()
        file.write("{} Counties in {}: \n".format(data.size, state))
        file.write(str(data) + "\n")

#This is a bar graph sorts by years and states
def bar1():
    # just change this number to change how many it shows
    index = 50
    for year in years:
        data = df.loc[(df['YYYY'] == year)]
        for i in range(index, 3500, index):
            data = data.loc[(data["TotalDrugReportsCounty"] <= i) & (data["TotalDrugReportsCounty"] >= i-index)]
            data = data.sort_values('TotalDrugReportsCounty', ascending = True)
            if not data.empty:
                ax = data.plot.bar(x='FIPS_Combined', y='TotalDrugReportsCounty', )
                plt.title("Total Drug Reports In {}".format(year))
                plt.tick_params(labelsize=5)
                plt.tight_layout()
                plt.show()

#This is a bar graph sorts by years
def bar2():
    index = 50
    for year in years:
        for state in states:
            data = df.loc[(df['YYYY'] == year) & (df["State"] == state)]
            for i in range(index, 3500, index):
                data = data.loc[(data["TotalDrugReportsCounty"] <= i) & (data["TotalDrugReportsCounty"] >= i-index)]
                data = data.sort_values('TotalDrugReportsCounty', ascending = True)
                if not data.empty:
                    ax = data.plot.bar(x='FIPS_Combined', y='TotalDrugReportsCounty', )
                    plt.title("Total Drug Reports For {} in {}".format(state, year))
                    plt.tick_params(labelsize=5)
                    plt.tight_layout()
                    plt.show()

#This is a histogram by state and year
def bar3():
    for year in years:
        for state in states:
            data = df.loc[(df['YYYY'] == year) & (df["State"] == state)]
            ax = data.hist(column='TotalDrugReportsCounty', bins=1000)
            plt.title("Total Drug Reports For {} in {}".format(state, year))
            plt.tick_params(labelsize=5)
            plt.tight_layout()
            plt.savefig('{}_{}'.format(year, state))

#This is a histogram year
def bar4():
    for year in years:
        data = df.loc[(df['YYYY'] == year)]
        ax = data.hist(column='TotalDrugReportsCounty', bins=1000)
        plt.title("Total Drug Reports In {}".format(year))
        plt.tick_params(labelsize=5)
        plt.tight_layout()
        plt.savefig("{}".format(year))

#report1()
#report2()
report3()
#bar1()
#bar2()
#bar3()
#bar4()
