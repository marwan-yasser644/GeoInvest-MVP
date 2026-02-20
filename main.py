from init_db import init_database
from scraper import fetch_and_save_data

def run_project():
    print("Starting GeoInvest MVP Process...")
    
    init_database()
    
  # جرب هذا المسمى بدلاً من القديم في main.py
    target_area = "الشيخ زايد"
    categories = ["cafe", "pharmacy", "restaurant"]
    
    for category in categories:
        try:
            fetch_and_save_data(target_area, category)
        except Exception as e:
            print(f"Error fetching {category}: {e}")
            
    print("Project execution completed.")

if __name__ == "__main__":
    run_project()