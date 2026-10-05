# 1. Class for Medicine
class Medicine:
    def __init__(self, name: str, stock: int, price: float):
        self.name = name
        self.stock = stock
        self.price = price

    def is_available(self) -> bool:
        return self.stock > 0


# 2. Class for Pharmacy
class Pharmacy:
    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        self.inventory = []

    def add_medicine(self, medicine: Medicine):
        self.inventory.append(medicine)

    def search_medicine(self, med_name: str):
        print(f"\n--- Searching for '{med_name}' at {self.name} ({self.location}) ---")
        for item in self.inventory:
            if item.name.lower() == med_name.lower():
                if item.is_available():
                    print(f"SUCCESS: {item.name} is AVAILABLE!")
                    print(f"Stock: {item.stock} | Price per unit: LKR {item.price}")
                else:
                    print(f"OUT OF STOCK: {item.name} is currently unavailable.")
                return
        
        print(f"NOT FOUND: {med_name} is not carried by this pharmacy.")


# Testing Application Logic
if __name__ == "__main__":
    my_pharmacy = Pharmacy("City Care Pharmacy", "Colombo 03")

    med1 = Medicine("Panadol", 50, 20.0)
    med2 = Medicine("Amoxicillin", 0, 45.0)
    med3 = Medicine("Vitamin C", 15, 10.0)

    my_pharmacy.add_medicine(med1)
    my_pharmacy.add_medicine(med2)
    my_pharmacy.add_medicine(med3)

    search_query = input("Enter medicine name to search: ")
    my_pharmacy.search_medicine(search_query)