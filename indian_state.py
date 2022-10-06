import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static
#import geopandas as gpd


st.set_page_config(layout="wide")

df_1  = f'states_india.geojson'


m = folium.Map(location=[23.47,77.94],tiles='CartoDB positron',name="Light Map",zoom_start=5,attr="My Data attribution")

#india_covid = f"covid_cases_india.csv"
df = pd.read_csv('covid_cases_india.csv')

choice = ['Confirmed Cases', 'Active Cases', 'Cured/Discharged','Death']
choice_selected = st.selectbox("Select choice",choice)

folium.Choropleth(
	geo_data=df_1,
	name="choropleth",
	data = df ,
	columns=["state_code",choice_selected],
	key_on="feature.properties.state_code",
	fill_color="YlOrRd",
	fill_opacity=0.7, 
	line_opacity = .1, 
	legend_name=choice_selected
	).add_to(m)

#folium.features.GeoJson(df_1, name="States",).add_to(m)
folium.LayerControl().add_to(m)
folium_static(m,width=1600,height=950)	
