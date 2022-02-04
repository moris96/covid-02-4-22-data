import plotly.express as px
import pandas as pd

# pandas data
df = pd.read_csv('data sets/coviddata.csv')
print(df.head())

fig = px.scatter_3d(df, x='Cases', y='Deaths', z='Population', color='Country', title='COVID-19 Data as of 02/4/2022')

fig.show()