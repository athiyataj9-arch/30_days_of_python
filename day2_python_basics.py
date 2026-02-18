"""
Day 2 - Python Data Structures & Control Flow
Author: Athiya
Focus: Moving from single variables to collections of data.
"""

# 1. Advanced List Operations (The precursor to NumPy Arrays)
# Creating a list of data science skills
skills = ["Python", "Statistics", "Machine Learning"]
skills.append("Data Visualization")
skills.insert(1, "SQL") # Adding SQL at index 1

print("--- Day 2: Data Structures ---")
print(f"My Skill Stack: {skills}")
print(f"Primary Skill: {skills[0]}") # Indexing


# 2. Dictionaries (The precursor to Pandas Series/DataFrames)
# Storing data as Key-Value pairs
dataset_info = {
    "name": "Titanic",
    "size_mb": 1.2,
    "features": 12,
    "is_cleaned": False
}

print(f"\nAnalyzing Dataset: {dataset_info['name']}")
print(f"Dataset Features: {dataset_info.get('features')}")


# 3. Control Flow: Logic for Data Cleaning
# Categorizing numbers (Simulating outlier detection)
data_points = [10, 50, 200, 35, 150]
cleaned_data = []

print("\nRunning Data Quality Check...")
for point in data_points:
    if point > 100:
        print(f"-> Outlier detected: {point} (Skipping)")
    else:
        cleaned_data.append(point)

print(f"Final Cleaned List: {cleaned_data}")


# 4. Functions for Reusable Logic
def calculate_accuracy(y_true, y_pred):
    """Simple function to simulate ML accuracy calculation."""
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return (correct / len(y_true)) * 100

actual = [1, 0, 1, 1]
predicted = [1, 0, 0, 1]
print(f"\nModel Accuracy: {calculate_accuracy(actual, predicted)}%")