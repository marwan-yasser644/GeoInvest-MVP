import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
import folium
from streamlit_folium import folium_static
from folium.plugins import HeatMap

load_dotenv()

st.set_page_config(page_title="GeoInvest AI Dashboard", layout="wide")

st.title("🌍 GeoInvest AI: Investment Opportunities")
st.sidebar.header("Control Panel")

def get_data():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    query = "SELECT name, category, latitude, longitude FROM locations"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

try:
    df = get_data()

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Locations", len(df))
    col2.metric("Top Category", df['category'].mode()[0])
    col3.metric("Opportunity Score", "85%")

    # Map Selection
    st.subheader("Investment Heatmap")
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=14)
    
    heat_data = df[['latitude', 'longitude']].values.tolist()
    HeatMap(heat_data).add_to(m)
    
    for _, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=5,
            popup=row['name'],
            color="red" if row['category'] == 'restaurant' else "blue",
            fill=True
        ).add_to(m)

    folium_static(m)

    # Data Table
    st.subheader("Raw Analysis Data")
    st.dataframe(df)

except Exception as e:
    st.error(f"Waiting for data... Run your scraper first! Error: {e}")