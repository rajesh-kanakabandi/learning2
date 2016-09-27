"""
    block: is a piece of code that performs a set of instructions.
    function: is a block of code that performs a specific task

    syntax:
    definition:
    def func_name(arguments):
        function body
        faksdfjhakfasf
        return
    #end of function.

    access:
    func_name(argumetns)

    call by value, call by reference.
    call by value:
        func_name(12,10, True)
        12,10, True, primitive types are literal values.
        no object references.
    call by reference:
        func_name(a,b,c)
        a,b,c are objects with references.
        changes to a, b,c will persist after the function call.

    arguments:
    regular arguments, keyword or default or optional arguments
    regular arguments:
        def func_name(a,b):
        func_name(10,10)
        func_name(a=10, b=10)
        func_name(b=10, a=10)

    keyword argumetns:
        def func_name(a=0, b=0):
        func_name(5,10)
        func_name(a=5, b=10)
        func_name(b=10, a=5)
    combination of regular and keyword arguments:
        def func_name(a,b,c=0,d=10):

        func_name(5,10,5,10)
        func_name(5,10, d=5)
        func_name(a=5, b=10, d=5)
        func_name(5,10,15)

def func1():
    pass

def func2():
    pass

def func3():
    func1()
    func2()

Assignment:
(1, 2, 3, 4, 5, 6, 7, 8, 9) find the number of evens and odds.
 Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
Sample Output :
fizzbuzz
1
2
fizz
4
buzz

"""

def even_odds(input_list):
    even_count = 0
    odd_count = 0
    for n in input_list:
        if n%2 == 0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count,odd_count)
print(even_odds([1,2,3,4,5,6,7,8,9]))


def celToFar(temp_in_cel):
    #temp_in_farenheit = (9*temp_in_cel + 160)/5
    temp_in_farenheit = (9*temp_in_cel/5) + 32
    return temp_in_farenheit



print(celToFar(60))

def farToCel(temp_in_far):
    #temp_in_cel = (5*temp_in_far - 160)/9
    temp_in_cel = (temp_in_far - 32) * 5/9
    return temp_in_cel

print(farToCel(140))
# def swap(a,b):
#     c =  a
#     a = b
#     b = c
#     return (a,b)
# swap(a,b)

# def func1(a):
#     a += [2]
#     print(a)
#     return a
#
# a = [1]
# print(a)
# func1(a)
# print(a)
#
# def func2(str1):
#     str1 = str1 + str1
#     print(str1)
#
# a = "hello"
# print(a)
# func2(a)
# print(a)
#

# def func_name(a,b,c=0,d=10):
#     print("a : {}, b: {}, c: {}, d: {}".format(a,b,c,d))
#
# func_name(5,10,5,10)
# func_name(5,10, d=5)
# func_name(a=5, b=10, d=5)
# func_name(5,10,15)
