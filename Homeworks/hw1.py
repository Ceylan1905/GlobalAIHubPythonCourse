# -*- coding: utf-8 -*-
"""HW1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QsgF-vOW50uaJ5AedZUM3z62tyLOO1qJ
"""

import random as rnd
matrix = [] # Initialize matrix
list=[] # Initialize list for add 9 prime numbers
k=0 # Define the variable for while loop 
n=0 # Define the variable for iteration

while k<9:
  r_number=rnd.randint(1,100) # Generate random number 1 between 100 
  if r_number > 1:
   for i in range(2,r_number):
       if r_number % i == 0: # Check for prime 
           break 
   else:
       k=k+1
       list.append(r_number) # Add random prime number to list


# Create 3x3 matrix from list's items
for i in range(3):  
    a =[] 
    for j in range(3):     
         a.append(list[n])
         n=n+1
    matrix.append(a)

  
# For printing the matrix 
print("My 3x3 matris is: \n")
for i in range(3): 
    for j in range(3): 
        print(matrix[i][j], end = " ") 
    print()