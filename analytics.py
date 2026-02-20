import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def generate_investment_report():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        port=os.getenv("DB_PORT")
    )
    
    query = "SELECT category, COUNT(*) as total FROM locations GROUP BY category;"
    df = pd.read_sql(query, conn)
    
    print("--- Investment Opportunity Analysis ---")
    for index, row in df.iterrows():
        print(f"Category: {row['category']} | Existing Businesses: {row['total']}")
    
    if 'pharmacy' not in df['category'].values or df[df['category'] == 'pharmacy']['total'].values[0] == 0:
        print("\nGOLDEN OPPORTUNITY: High demand for Pharmacies in this sector!")
    
    conn.close()

if __name__ == "__main__":
    generate_investment_report()