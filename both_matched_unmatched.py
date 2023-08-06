def find_matched_and_unmatched_values(dict1, dict2):
    matched_values = {}
    unmatched_values = {}

    for key, value in dict1.items():
        if key in dict2 and dict2[key] == value:
            matched_values[key] = value
        else:
            unmatched_values[key] = value

    for key, value in dict2.items():
        if key not in dict1:
            unmatched_values[key] = value

    return matched_values, unmatched_values

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

# Finding matched and unmatched values
matched_values, unmatched_values = find_matched_and_unmatched_values(dict1, dict2)

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
print("Matched key-value pairs:", matched_values)
print("Unmatched key-value pairs:", unmatched_values)
