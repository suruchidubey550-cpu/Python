'''
Tuples in Python are similar to lists, but they are immutable, meaning that once a tuple is created, its elements cannot be changed, 
 added, or removed. Tuples are defined by enclosing elements in parentheses `()`.
 '''
# a = (1, 2, 3, 4, 5)
# print(a[0])  # Output: 1
# print(type(a))  # Output: <class 'tuple'>
# n = a.count(2)  # Counts the occurrences of 2 in the tuple
# print(n)  # Output: 1 
# i = a.index(3)  # Returns the index of the first occurrence of 3
# print(i)  # Output: 2

#Tuple methods
t1 = (1, 2, 3, 4, 5)
print(t1.count(2))  # Output: 1
print(t1.index(3))  # Output: 2
print(t1)  # Output: (1, 2, 3, 4, 5)
'''Tuples has only two built-in methods: count() and index().
 Tuples are often used to group related data together, and they can be used as keys in dictionaries because they are hashable.
 Tuples can also be used to return multiple values from a function, and they can be unpacked into individual variables.'''

#Oprations on tuples
t1 = (1, 2, 3)
print(t1[0])  # Output: 1#indexing
print(t1[0:2])  # Output: (1, 2)#slicing
print(t1 + (4, 5))  # Output: (1, 2, 3, 4, 5)#concatenation
print(t1 * 2)  # Output: (1, 2, 3, 1, 2, 3)#repetition
print(len(t1))  # Output: 3#length
print(3 in t1)  # Output: True#membership
print(max(t1))  # Output: 3#maximum
print(min(t1))  # Output: 1#minimum
print(sum(t1))  # Output: 6#sum
print(sorted(t1))  # Output: [1, 2, 3]#sorting
print(tuple(sorted(t1)))  # Output: (1, 2, 3)#sorting and converting back to tuple
print(t1[::-1])  # Output: (3, 2, 1)#reversing
print(t1.count(2))  # Output: 1#counting occurrences
print(t1.index(3))  # Output: 2#finding index
print(t1.__sizeof__())  # Output: size of the tuple in bytes
print(t1.__len__())  # Output: 3#length using __len__()
print(t1.__contains__(2))  # Output: True#membership using __contains__()
complex_tuple = (1, 2, (3, 4), [5, 6], {7: 'seven', 8: 'eight'})
print(complex_tuple[2][0])  # Output: 3#accessing nested    


