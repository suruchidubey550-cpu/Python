'''
Dictionary is a collection of key-value pairs. Each key is unique and maps to a specific value. Dictionaries are mutable, meaning they can be
changed after creation. They are defined using curly braces {} and consist of key-value pairs separated by colons.
Dictionaries are unordered, meaning that the items do not have a defined order. However, starting from Python 3.7, dictionaries maintain
the insertion order of items.Dictionaries are useful for storing and retrieving data based on unique keys,
 making them a powerful data structure in Python.They are unordered,and indexed,and cannot contain duplicate vakues.

'''
# # Creating a dictionary
my_dict = {
 "name": "Suruchi",
 "age": 25,
 "city": "India"
}
# print(my_dict)  # Output: {'name': 'Suruchi', 'age': 25, 'city': 'India'}
# # Accessing values using keys
# print(my_dict["name"])  # Output: Suruchi

# #Dictionary methods
# print(my_dict.get("age"))  # Output: 25
# print(my_dict.get("country", "Not Found"))  # Output: Not Found
# print(my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
# print(my_dict.values())  # Output: dict_values(['Suruchi', 25, 'India'])
# print(my_dict.items())  # Output: dict_items([('name', 'Suruchi'), ('age', 25), ('city', 'India')])
# print(my_dict.update({"Friend":"Alice"}))  # Output: None

# # Adding a new key-value pair
# my_dict["country"] = "USA"
# print(my_dict)  # Output: {'name': 'Suruchi', 'age': 25, 'city': 'India', 'country': 'USA'}
# print(my_dict.pop("age"))  # Output: 25
# print(my_dict)  # Output: {'name': 'Suruchi', 'city': 'India', 'country': 'USA'}
# print(my_dict.popitem())  # Output: ('country', 'USA')
# print(my_dict.clear())  # Output: None
# print(my_dict.setdefault("age", 30))  # Output: 30
print(my_dict.copy())  # Output: {'name': 'Suruchi', 'age': 25, 'city': 'India'}


#using dictionary comprehension
squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#using for loop to iterate through dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Suruchi, age: 25, city: India

    d = { }#Empty dictionary
    student = {
        "name": "Suruchi",
        "age": 25,
    }
    student.setdefault("city", "India")  # Adds "city" key with value "India" if it doesn't exist
    print(student)  # Output: {'name': 'Suruchi', 'age': 25, 'city': 'India'}
    
