# data_collections.py

# Saraksta piemērs
fruits = ["apple", "banana", "cherry", "date"]

# Filtrē sarakstu pēc garuma > 5
long_fruits = [f for f in fruits if len(f) > 5]

# Vārdnīcas piemērs
ages = {"Kristaps": 42, "Anna": 30, "Jānis": 25}

# Iterācija pa vārdnīcu
for name, age in ages.items():
    print(f"{name} is {age} years old")

# Kombinēšana
combined = list(zip(fruits, ages.keys()))
print(combined)