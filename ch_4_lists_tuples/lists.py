# #list indexing and slicing
# my_list = [10, 20, 30.3, 446, False ,"Suruchi"]
# print(my_list[0])  # Output: 10
# print(my_list[5])  # Output: "Suruchi"
# print(my_list[0:2]) # Output: [10, 20]
# # 1 - D ----> [start:stop:step]
# print(my_list[0:6:2]) # Output: [10, 30.3, False]
# print(my_list[-1]) # Output: "Suruchi"
# print(my_list[-6:-1]) # Output: [10, 20, 30.3, 446, False]
# # print(my_list[-6:-1:2]) # Output: [10, 30.3, False]
# print(my_list[::-1]) # Output: [False, 446, 30.3, 20, 10]
# print(my_list[::-2]) # Output: [10, 30.3, False]

# # 2 - D ----> [row_start:row_stop:row_step][column_start:column_stop:column_step]
# #For 2 -D arrys slicing we use numpy library
# import numpy as np
# a = np.array([[1, 2, 3],
#               [4, 5, 6], 
#               [7, 8, 9]
#          ])
# print(a[0:2]) # Output: [[1 2] [4 5]]
# print(a[:, 1]) # Output: [2 5 8]
# print(a[1:, 1:]) # Output: [[5 6] [8 9]]
# print(a[::2, ::2]) # Output: [[1 3] [7 9]]
# print(a[::-1, ::-1]) # Output: [[9 8 7] [6 5 4] [3 2 1]]
# print(a[:, 0:2]) # Output: [[1 2] [4 5] [7 8]]
# print(a[1, :]) # Output: [4 5 6]
# print(a[1, 2]) # Output: 6
# print(a[1:, 1:3]) # Output: [[5 6] [8 9]]
# print(a[::2, 1:]) # Output: [[2 3] [8 9]]
# print(a[0:2, 1:3]) # Output: [[2 3] [5 6]]
# print(a[0:2, 1:3]) # Output: [[4 5] [7 8]]
# print(a[:, :]) # Output: [[1 2 3] [4 5 6] [7 8 9]]
# print(a[::-1]) # Output: [[9 8 7] [6 5 4] [3 2 1]]
# print(a[:, ::-1]) # Output: [[9 8 7] [6 5 4] [3 2 1]]
# friends = ["Apple", "Orange", 5 , 345.06,False, "Rakesh"]
# print(friends[0]) # Output: "Apple"
# friends[0] = "Banana"
# print(friends) # Output: ["Banana", "Orange", 5 , 345
'''
lists are mutable, meaning you can change their content without changing their identity.
 You can add, remove, or modify elements in a list after it has been created.
 
 '''
#Lists methods
l1 = [1, 2, 3, 4, 5]
print(l1.append(6))  # Adds 6 to the end of the list
print(l1.insert(2, 2.5))  # Inserts 2.5 at index 2
print(l1.remove(3))  # Removes the first occurrence of 3
print(l1.pop())  # Removes and returns the last item (6)
print(l1.sort())  # Sorts the list in ascending order
print(l1.reverse())  # Reverses the list
print(l1.copy())  # Creates a shallow copy of the list
print(l1.clear())  # Removes all items from the list
print(l1.count(2))  # Counts the occurrences of 2 in the list
print(l1.index(2))  # Returns the index of the first occurrence of 2
print(l1.extend([7, 8, 9]))  # Extends the list by appending elements from another list



