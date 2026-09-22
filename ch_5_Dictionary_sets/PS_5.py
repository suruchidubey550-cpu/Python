# #Q.1 WAAP to craete a dictionary of hindi words with values as their English translations .Provide user with an option to look it up!
# words ={
#     "madad": "help",
#     "pani": "water",
#     "kurti": "shirt",
# }
# word = input("Enter a word to get its meaning: ")
# print(words.get(word, "Word not found in the dictionary."))# ------> print(words[word])

#Q.2 WAAP to input 8 numbers from the user and display all the unique numbers(once)
# -----> we used sets for this questiom because sets only store unique values and automatically remove duplicates.

# s = set()
# n =(input("Enter number1: "))
# s.add(int(n))
# n =(input("Enter number2: "))
# s.add(int(n))
# n =(input("Enter number3: "))
# s.add(int(n))
# n =(input("Enter number4: "))
# s.add(int(n))
# n =(input("Enter number5: "))
# s.add(int(n))
# n =(input("Enter number6: "))
# s.add(int(n))
# print(s)

# #Q.3 Can we have a set with 18(int) and '18'(str) as a value in it?
# s = set()
# s.add(18)
# s.add("18")
# print(s)

#Q.4 What will be the length of the following set s ?
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s) #output only 20 and '21' because 20 == 20.0 (Here it checks value not data type)

#Q.5 Create an empty dictionary. Allow 4 friends to enter thier favorite language as value and use key as their names .
#  Assume that the names are unique.
# d = {}
# name = input("Enter friend1 name: ")
# lang = input("Enter language name: ")
# d.update({name : lang})

# name = input("Enter friend2 name: ")
# lang = input("Enter language name: ")
# d.update({name : lang})

# name = input("Enter friend3 name: ")
# lang = input("Enter language name: ")
# d.update({name : lang})

# name = input("Enter friend4 name: ")
# lang = input("Enter language name: ")
# # d.update({name : lang}) 
# print(d)

# Q.6 If the names of two friends are same ; What will happen to the program in problem 5?
'''ANS: If the names of two friends are same the first one lang , which was entered will be updated to the recent entered language 
Rohan-->C
Rohan-->Java
{'Rohan':'Java'}
'''
#Q.7  If the languages of two friends are same ; What will happen to the program in problem 5?
'''ANS: In dictionary same values are possible , like If the languages of two friends are same, it will also show the same 
'''
#Q.8 Can you change the values inside a ist which is contained in set s?
s = {8, 7, 12, "Suruchi", [1,2]}
#Indexing is not possible in sets --> and we can't change values inside a list containg set
