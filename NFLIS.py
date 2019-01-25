import pandas as pd
import plotly

data = pd.read_excel('2018_MCMProblemC_DATA/MCM_NFLIS_Data.xlsx')
print(data)

layout = dict(
        title = 'NFLIS Data',
        showlegend = True,
        geo = dict(
            scope='usa',
            projection=dict( type='albers usa' ),
            showland = True,
            landcolor = 'rgb(217, 217, 217)',
            subunitwidth=1,
            countrywidth=1,
            subunitcolor="rgb(255, 255, 255)",
            countrycolor="rgb(255, 255, 255)"
        ),
    )
fig = dict(data=cities, layout=layout)
