# Q.1 WAP to find greatest of four numbers
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))
# d = int(input("Enter fourth number : "))

# if(a>b and a>c and a>d):
#     print("a is greater.")
# elif(b>a and b>c and b>d):
#     print("b is greater.")
# elif(c>a and c>b and c>d):
#     print("c is greater.")
# else:
#     print("d is greater.")

''' Q.2 WAP to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass.
 Assume 3 subjects and take marks as an input from the user'''

maths = int(input("Enter marks of maths : "))
physics = int(input("Enter marks of physics : "))
chemistry = int(input("Enter marks of chemistry : "))

# Total percentage 
total_percentage = (maths + physics + chemistry)/3
print(total_percentage)

if(total_percentage >= 40 and maths>=33 and physics >= 33 and chemistry >= 33):
    print("You are pass!")
else:
    print("You failed, better luck next time!")

