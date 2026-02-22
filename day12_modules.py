# ==========================================
# DAY 12: MODULES & PACKAGES 📦
# ==========================================

import math
import random
from datetime import datetime

# 1. USING BUILT-IN MODULES
print(f"Value of Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")

# 2. GENERATING RANDOM DATA (Great for Data Science simulations)
data_points = [random.randint(1, 100) for _ in range(5)]
print(f"\nRandom Data Points: {data_points}")
print(f"Random Choice: {random.choice(['Success', 'Failure', 'Pending'])}")

# 3. DATETIME MODULE
now = datetime.now()
print(f"\nCurrent Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 4. NOTE ON EXTERNAL PACKAGES (pip)
# To install new tools, we use: pip install requests pandas numpy
print("\nReady to explore external libraries in the next section!")

# End of Day 12 Script