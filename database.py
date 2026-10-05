import sqlite3

def init_db():
    """Funtion for create Database & Tables """
    conn = sqlite3.connect("pharmacy.db")
    cursor = conn.cursor()

    # 1. create the Pharmacies Table 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pharmacies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

    # 2. create the Medicines Table (Relational Key: pharmacy_id)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            stock INTEGER NOT NULL,
            price REAL NOT NULL,
            pharmacy_id INTEGER,
            FOREIGN KEY (pharmacy_id) REFERENCES pharmacies (id)
        )
    ''')

    conn.commit()
    conn.close()

def seed_sample_data():
    """collect the data sample for Testing """
    conn = sqlite3.connect("pharmacy.db")
    cursor = conn.cursor()

    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM pharmacies")
    if cursor.fetchone()[0] == 0:
        # Insert Sample Pharmacy
        cursor.execute("INSERT INTO pharmacies (name, location) VALUES ('City Care Pharmacy', 'Colombo 03')")
        pharmacy_id = cursor.lastrowid

        # Insert Sample Medicines linked to Pharmacy
        cursor.execute("INSERT INTO medicines (name, stock, price, pharmacy_id) VALUES (?, ?, ?, ?)", ("Panadol", 50, 20.0, pharmacy_id))
        cursor.execute("INSERT INTO medicines (name, stock, price, pharmacy_id) VALUES (?, ?, ?, ?)", ("Amoxicillin", 0, 45.0, pharmacy_id))
        cursor.execute("INSERT INTO medicines (name, stock, price, pharmacy_id) VALUES (?, ?, ?, ?)", ("Vitamin C", 15, 10.0, pharmacy_id))

        conn.commit()
        print("Sample data successfully added to SQLite Database!")

    conn.close()

if __name__ == "__main__":
    init_db()
    seed_sample_data()