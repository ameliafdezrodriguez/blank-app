import streamlit as st

st.title("🎈 My new app")
st.write(
    "This is my new app"
)

import streamlit as st
from streamlit_folium import st_folium
import folium

# Title
st.title("WMS Map Viewer")

# WMS Service Details
wms_url = "https://www.geo-futurewater.eu/geoserver/gaz/wms?service=WMS"
wms_layer = "PPERC"

# Create a Folium Map
m = folium.Map(location=[0, 0], zoom_start=10)

# Add WMS Layer
folium.raster_layers.WmsTileLayer(
    url=wms_url,
    name="WMS Layer",
    layers=wms_layer,
    fmt="image/png",
    transparent=True,
    version="1.1.1",
).add_to(m)

# Add Layer Control
folium.LayerControl().add_to(m)

# Display Map in Streamlit
st_data = st_folium(m, width=800, height=600)