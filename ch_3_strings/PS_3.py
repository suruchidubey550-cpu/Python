# #Q.1 greeting
# name = input("Enter your name: ")
# print(f"Hello {name}, welcome to the world of Python programming!")

# #Q.2 using replace function
# letter = '''Dear <|NAME|>,
# You are selected!
# <|DATE|>'''
# print(letter.replace("<|NAME|>", name).replace("<|DATE|>", "1st January 2024"))

# #Q.3 white space detect
# name = "  Suruchi is going to be a great    programmer"
# print(name.find("  "))

#Q.4 Escape sequence characters
letter = "Dear Suruchi,\n\t this Python course is nice. \nThanks!"
print(letter)

'''Strings in Python are immutable, meaning that once a string is created, it cannot be changed.
 You can create new strings based on existing ones, but you cannot modify the original string in place
'''