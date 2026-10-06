from fastapi import FastAPI, HTTPException
import sqlite3

app = FastAPI(
    title="Medicine Reminder & Pharmacy Matcher API",
    version="1.0.0"
)

DB_NAME = "pharmacy.db"

@app.get("/")
def home():
    """API Health Check Endpoint"""
    return {"message": "Pharmacy Matcher API is running successfully!"}

@app.get("/medicines/search")
def search_medicine(name: str):
    """Search medicine across pharmacies via API Endpoint"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    query = '''
        SELECT m.name, m.stock, m.price, p.name, p.location
        FROM medicines m
        JOIN pharmacies p ON m.pharmacy_id = p.id
        WHERE LOWER(m.name) = LOWER(?)
    '''
    
    cursor.execute(query, (name,))
    results = cursor.fetchall()
    conn.close()

    if not results:
        raise HTTPException(status_code=404, detail=f"Medicine '{name}' not found.")

    response_data = []
    for row in results:
        med_title, stock, price, pharm_name, location = row
        response_data.append({
            "medicine_name": med_title,
            "stock": stock,
            "price_lkr": price,
            "pharmacy_name": pharm_name,
            "location": location,
            "is_available": stock > 0
        })

    return {"query": name, "results": response_data}