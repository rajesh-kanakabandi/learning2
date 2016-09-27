"""
write a function to check if a given number is a prime.
prime numbers are whole numbers that do not have any factors.
n-1 - 2
"""

def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(6))


"""
Write a function to find the largest prime less than n.
"""

def largest_prime(n):
    for i in range(n,2,-1):
        if is_prime(i):
            return i

print(largest_prime(100))

"""
(x1,y1) (x2,y2)
distance between 1 and 2 is srt[(x1-x2)^2 + (y1-y2)^2]

"""
import math
def distance(a,b):
    dist = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return dist


print(distance((1,2), (2,1)))

"""
find the area of a circle.
"""
from math import pi
def area_of_circle(r):
    return pi*r**2

print(area_of_circle(1))

"""
write a function to sort a list of integers.
3,2,4,5,3,2,6

2,3,4,5,3,2,6
2,2,3,3,4,5,6

pivot = i
j

i= 0; j = 1...n-1
i = 1; j = 2...n-1
.
.
n-2
"""

def sort_list(num_list):
    for i in range(0,len(num_list)-2):
        for j in range(i+1,len(num_list)-1):
            if (num_list[i]>num_list[j]):
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list


print(sort_list([3,2,4,5,3,2,6]))

"""
write a function to sort a list in descending order.
"""


"""
    write a functions to implement queue functions on a list.
    [1,2,3] -> insert 4 = [1,2,3,4]
    [1,2,3] -> pop = [2,3,4] returns 1.

    research about global key word in python.

"""
queue = []
def insert(value):

def pop():
