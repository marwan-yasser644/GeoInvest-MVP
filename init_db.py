import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_database():
    try:
        # الاتصال بقاعدة بيانات Neon
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            port=os.getenv("DB_PORT")
        )
        cur = conn.cursor()
        
        print("🛠️ Creating table 'locations'...")
        # 1. إنشاء الجدول لو مش موجود
        cur.execute("""
            CREATE TABLE IF NOT EXISTS locations (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) UNIQUE NOT NULL,
                category VARCHAR(100),
                latitude DOUBLE PRECISION,
                longitude DOUBLE PRECISION
            );
        """)

        # 2. تنظيف البيانات القديمة (اختياري)
        cur.execute("TRUNCATE TABLE locations RESTART IDENTITY;")

        # 3. إضافة البيانات الأولية للشيخ زايد
        sample_data = [
            ('Arkan Plaza', 'Mall', 30.0125, 30.9850),
            ('Capital Business Park', 'Business', 30.0180, 30.9780),
            ('Starbucks Zayed', 'Cafe', 30.0150, 30.9820),
            ('Mall of Arabia', 'Mall', 30.0075, 30.9650),
            ('Galleria 40', 'Mall', 30.0110, 30.9800),
            ('The Lane', 'Restaurant', 30.0135, 30.9835)
        ]

        print("📥 Inserting sample data...")
        cur.executemany("""
            INSERT INTO locations (name, category, latitude, longitude) 
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING;
        """, sample_data)

        conn.commit()
        cur.close()
        conn.close()
        print("✅ Database Initialized Successfully on Cloud!")

    except Exception as e:
        print(f"❌ Error during initialization: {e}")

if __name__ == "__main__":
    initialize_database()