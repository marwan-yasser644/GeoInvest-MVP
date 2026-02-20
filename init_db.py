import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def refill_data():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()
        
        # تنظيف الجدول أولاً عشان ما نكررش
        cur.execute("TRUNCATE TABLE locations;")

        # إضافة 6 محلات متنوعة (مولات، كافيهات، مطاعم)
        sample_data = [
            ('Arkan Plaza', 'Mall', 30.0125, 30.9850),
            ('Capital Business Park', 'Business', 30.0180, 30.9780),
            ('Starbucks Zayed', 'Cafe', 30.0150, 30.9820),
            ('Mall of Arabia', 'Mall', 30.0075, 30.9650),
            ('Galleria 40', 'Mall', 30.0110, 30.9800),
            ('The Lane', 'Restaurant', 30.0135, 30.9835)
        ]

        cur.executemany("""
            INSERT INTO locations (name, category, latitude, longitude) 
            VALUES (%s, %s, %s, %s)
        """, sample_data)

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Data Refilled: 6 Locations added. Accuracy should be 100% now!")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    refill_data()