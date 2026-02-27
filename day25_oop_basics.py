# ==========================================
# DAY 25: OBJECT-ORIENTED PROGRAMMING (OOP) 🏗️
# ==========================================

# 1. DEFINING A CLASS (The Blueprint)
class Smartphone:
    # The Constructor: Runs when a new object is created
    def __init__(self, brand, model, battery_level):
        self.brand = brand          # Attribute
        self.model = model          # Attribute
        self.battery = battery_level # Attribute

    # A Method: A function that belongs to the class
    def check_status(self):
        return f"{self.brand} {self.model} is at {self.battery}% battery."

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"Charging... Current battery: {self.battery}%")

# 2. CREATING OBJECTS (Instances of the Blueprint)
phone1 = Smartphone("Apple", "iPhone 15", 45)
phone2 = Smartphone("Samsung", "Galaxy S23", 10)

# 3. ACCESSING DATA & CALLING METHODS
print(phone1.check_status())
phone2.charge(30)
print(phone2.check_status())

# 4. CHANGING ATTRIBUTES DIRECTLY
phone1.battery = 100
print(f"After manual update: {phone1.check_status()}")