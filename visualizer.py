import psycopg2
import folium
from folium.plugins import HeatMap
import os
from dotenv import load_dotenv

load_dotenv()

def create_map():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()

    # Get all locations
    cur.execute("SELECT name, latitude, longitude, category FROM locations;")
    rows = cur.fetchall()

    # Create base map at Sheikh Zayed coordinates
    m = folium.Map(location=[30.0444, 30.9833], zoom_start=14, tiles="OpenStreetMap")

    heat_data = []
    for row in rows:
        name, lat, lon, cat = row
        # Add markers for each business
        color = "blue" if cat == "cafe" else "red"
        folium.Marker(
            location=[lat, lon],
            popup=f"{name} ({cat})",
            icon=folium.Icon(color=color)
        ).add_to(m)
        heat_data.append([lat, lon])

    # Add HeatMap layer to show density
    HeatMap(heat_data).add_to(m)

    # Save to HTML
    m.save("investment_map.html")
    print("Success! Investment map has been generated as 'investment_map.html'")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_map()