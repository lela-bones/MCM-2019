import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

twoten = pd.read_csv('Data/ACS_10_5YR_DP02_with_ann.csv')
twoeleven = pd.read_csv('Data/ACS_11_5YR_DP02_with_ann.csv')
twotwelve = pd.read_csv('Data/ACS_12_5YR_DP02_with_ann.csv')
twothirteen = pd.read_csv('Data/ACS_13_5YR_DP02_with_ann.csv')
twofourteen = pd.read_csv('Data/ACS_14_5YR_DP02_with_ann.csv')
twofifteen = pd.read_csv('Data/ACS_15_5YR_DP02_with_ann.csv')
twosixteen= pd.read_csv('Data/ACS_16_5YR_DP02_with_ann.csv')

data = [twoten, twoeleven, twotwelve, twothirteen, twofourteen, twofifteen, twosixteen]

df = pd.concat(data)
print(df.head)
