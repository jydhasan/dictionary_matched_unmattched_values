def find_matched_values(dict1, dict2):
    matched_values = {}
    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            matched_values[key] = value
    return matched_values

# Example dictionaries
dict1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

dict2 = {
    "name": "John",
    "age": 25,
    "country": "USA"
}

# Finding matched values
matched_values = find_matched_values(dict1, dict2)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Matched key-value pairs:", matched_values)
