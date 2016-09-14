#data types
num = 1
num2 = 1.0
num3 = 123234234.2323

is_big = True
is_small = False

# num < num2
# out put is boolean

#if num:
#evaluates to True
#0, None, [], {}, set(), () evaluates to False
#everything else evaluates to True.

my_str = "hell"

#data structures

#lists
my_list = []
my_list1 = [1,2,3,4]
my_list2 = list()
my_list3 = list(set([1,2,3]))

print(dir(my_list)) # prints all available functions and attributes for list

#access by index. my_list[i]
#generate iterable lists by index my_list[start:stop:jump_length]

len(my_list) # get length of an iterable. len, sorted..etc are available to all iterable data structures.

#regular for loop
for num in my_list1:
    print(num)
#list comprehension

#pythonic way
my_list_reverse = my_list1[::-1]
#non pythonic way
my_list_reverse2 = [num for num in my_list1[::-1]]

print(my_list_reverse)
print(my_list_reverse2)

#sets

my_set = set()
my_set1 = set([])
my_set2 = set(my_list1)

# use - to perform difference

for num in my_set2:
    print(num)

#dict
my_dict = {}
my_dict1 = {'name': 'john', 'prof': 'IT'}

keys_list = [key for key, value in my_dict1.items()]
