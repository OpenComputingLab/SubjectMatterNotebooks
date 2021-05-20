# Geo Overview

Jupyter notebooks provide a natural home for embedded, interactive maps although we can also use embdded code to generate a wide range of static maps too.

A wide range of Python packages exist that support the creation and embedding of interactive maps built from third party mapping services such as OpenStreetMap (OSM).

Packages can also work with tiles served from a personally hosted map tile server.

## `ipyleaflet`

The [`ipyleaflet`](https://ipyleaflet.readthedocs.io/en/latest/) package supports the creation of embedded, interactive maps as an `ipywidget` using the [`leaflet.js`](https://leafletjs.com/) Javascript package.

%%capture
try:
    import ipyleaflet
except:
    %pip install ipyleaflet

import ipyleaflet as lflt

m = lflt.Map(center=[52.0250, -0.7084], zoom=14)
m

## `folium`

The [`folium`](https://python-visualization.github.io/folium/) package supports the creation and embedding of interactive maps using `leaflet.js` although in this case the embedded map is *not* wrapped as an `ipywidget`.

%%capture
try:
    import folium
except:
    %pip install folium

import folium

m = folium.Map(location=[52.0250, -0.7084], zoom_start=14)
m

### Adding Markers

Adding one or more markers to a map is relatively straightforward:

m = folium.Map(location=[52.0250, -0.7084], zoom_start=14, tiles='Stamen Toner')

folium.Marker([52.0250, -0.7084],
              popup='Open University, Walton Hall').add_to(m)
m

## Adding Boundaries

Boundaries represented using a `.geojson` file can be rendered as an overlayed map layer.

import os
m = folium.Map( location=[52.0250, -0.7084], zoom_start=9 )

#Path to geojson file
mk = os.path.join('boundaries', 'mk.json')

#Add geojson layer to map
folium.GeoJson( mk, name='geojson' ).add_to(m)

m

### Choropleth Maps

We can easily create a choropleth map from a tabular dataset that shares keys with a shapefile.

%%capture
try:
    import pandas
except:
    %pip install pandas

import pandas as pd

turnout=pd.read_csv('data/iw_turnout.csv')
turnout.head()

Various tools exist that allow us to read and process geojson files in a convenient way.

For example, use `fiona` to read in a geojson file, parse the extent of the shape file and find the mid-point:

%%capture
try:
    import fiona
except:
    %pip install fiona

import fiona

with fiona.open('boundaries/iw.json') as fi:
    latlong = [(fi.bounds[1]+fi.bounds[3])/2,
               (fi.bounds[0]+fi.bounds[2])/2]

Center the map on that mid-point and add a choropleth layer:

m = folium.Map(location=latlong )

folium.Choropleth(
   geo_data='boundaries/iw.json',
    data=turnout,
    columns=['Electoral Division', 'turnout'],
    key_on='feature.properties.WD13NM',
    fill_color='PuBuGn', fill_opacity=0.7
).add_to(m)

m

