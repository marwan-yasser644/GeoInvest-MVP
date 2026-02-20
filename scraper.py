import requests
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_and_save_data(area_name, amenity_type="cafe"):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()

    # We use radius search but keep the area_name for logging
    print(f"Fetching {amenity_type} data near {area_name}...")
    
    overpass_url = "http://overpass-api.de/api/interpreter"
    # Using fixed coordinates for Sheikh Zayed as a fallback
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="{amenity_type}"](around:5000, 30.0444, 30.9833);
      way["amenity"="{amenity_type}"](around:5000, 30.0444, 30.9833);
    );
    out center;
    """
    
    try:
        response = requests.get(overpass_url, params={'data': overpass_query})
        data = response.json()

        counter = 0
        for element in data.get('elements', []):
            name = element.get('tags', {}).get('name', 'Unnamed')
            lat = element.get('lat') or element.get('center', {}).get('lat')
            lon = element.get('lon') or element.get('center', {}).get('lon')
            
            cur.execute("""
                INSERT INTO locations (name, category, latitude, longitude, geom)
                VALUES (%s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
                ON CONFLICT DO NOTHING;
            """, (name, amenity_type, lat, lon, lon, lat))
            counter += 1

        conn.commit()
        print(f"Successfully saved {counter} locations to the database.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()