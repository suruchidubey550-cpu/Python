'''
Sets are unordered collections of unique elements. They are defined using curly braces {} or the set() constructor.
Sets are mutable, meaning they can be changed after creation. They do not allow duplicate values.They are onordered, and unindexed, 
and cannot contain duplicate values.

'''
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set with duplicate values
my_set = {1, 2, 2, 3, 3, 4, 4, 5, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

#Set methods
# Adding elements to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

#clearing a set
my_set.clear()
print(my_set)  # Output: set()

#copying a set
my_new_set = my_set.copy()
print(my_new_set)  # Output: set()

#Difference between two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.difference(set2))  # Output: {1, 2, 3}

#difference update between two sets
set1.difference_update(set2)
print(set1)  # Output: {1, 2, 3}

#discarding an element from a set
set1.discard(2)
print(set1)  # Output: {1, 3}

#operations on sets
#intersection of two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2))  # Output: {4, 5}

#union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))     # Output: {1, 2, 3, 4, 5}

#symmetric difference of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}

#issubset of a set
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))  # Output: True

#issuperset of a set
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3}
print(set1.issuperset(set2))  # Output: True

# popping an element from a set
set1 = {1, 2, 3, 4, 5}
print(set1.pop())  # Output: 1 (or any other element, since sets are unordered)

#clearing a set
set1.clear()
print(set1)  # Output: set()


