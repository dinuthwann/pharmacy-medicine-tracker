import sqlite3
from database import init_db, seed_sample_data

class PharmacyApp:
    def __init__(self, db_name="pharmacy.db"):
        self.db_name = db_name

    def search_medicine(self, med_name: str):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # SQL JOIN Query to search medicine across pharmacies
        query = '''
            SELECT m.name, m.stock, m.price, p.name, p.location
            FROM medicines m
            JOIN pharmacies p ON m.pharmacy_id = p.id
            WHERE LOWER(m.name) = LOWER(?)
        '''
        
        cursor.execute(query, (med_name,))
        results = cursor.fetchall()
        conn.close()

        print(f"\n--- Search Results for '{med_name}' ---")
        if not results:
            print(f"NOT FOUND: '{med_name}' is not available in any pharmacy database.")
            return

        for row in results:
            med_title, stock, price, pharm_name, location = row
            if stock > 0:
                print(f"AVAILABLE at [{pharm_name} - {location}]")
                print(f"Stock: {stock} units | Price: LKR {price}")
            else:
                print(f"OUT OF STOCK at [{pharm_name} - {location}]")

if __name__ == "__main__":
    #Initializing the database and sample data
    init_db()
    seed_sample_data()

    # Running the application
    app = PharmacyApp()
    search_query = input("Enter medicine name to search: ")
    app.search_medicine(search_query)