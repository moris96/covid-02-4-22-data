import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go
import pandas as pd



df = pd.read_csv('data sets/coviddata.csv')





# plotly go map fig
fig = go.Figure(go.Scattergeo(
    locationmode="country names",
    locations=df['Country'],
    text='Cases:' + df['Cases'] + '' + 'Deaths:' + df['Deaths'],

))

fig.update_geos(

    projection_type="orthographic",
    scope='world',
    resolution=50,
    showcountries=True, countrycolor="Black",
    showcoastlines=True, coastlinecolor="Black",
    showland=True, landcolor="LightGreen",
    showocean=True, oceancolor="LightBlue",
)
fig.update_layout(
    height=850,
    title="Data for COVID (Cases & Deaths)"
)


tabtitle = 'COVID-19 Data'
sourceurl = 'https://www.worldometers.info/coronavirus/'
githublink = 'https://github.com/moris96/covid-02-4-22-data'
image = 'corona.jpg'






# dash app layout
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = tabtitle

app.layout = html.Div([
    html.H1("COVID-19 Data: "),
    html.Img(src=app.get_asset_url(image)),
    dcc.Graph(figure=fig),
    html.A("Code on Github", href=githublink),
    html.A("Data Source", href=sourceurl),
])

# run app
app.run_server(debug=True)