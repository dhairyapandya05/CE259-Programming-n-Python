                                            # Assignment
# ID: 20CE071
# Name : Dhairya Pandya
# Aim : Study and Learn List, Tuple, Set and Dictionary 

# -----------------------------------------------------   Dictionary   -----------------------------------------------------

# a. Write a Python script to check whether a given key already exists in a dictionary.
#
d = {1:100, 2:200, 3:300, 4:400}
def is_there_key(k):
    if k in d:
        print('Key is present.')
    else:
        print('Key is not present.')
is_there_key(5)
is_there_key(2)

# b. Write a Python script to merge two Python dictionaries.
#
d1 = {'a':100, 'b':200}
d2 = {'c':300, 'd':400}
# naive approach
d3 = {}
d3 = d1.copy()
d3.update(d2)
print(d3)

# c. Write a Python program to sum all the items in a dictionary.
#
d = {1:100, 2:200, 3:300, 4:400}
def sum_items(d):
    sum = 0
    for i in d.values():
        sum += i
    return sum
print('Sum of items in {}: '.format(d), sum_items(d))

# d. Write a Python script to add a key to a dictionary.
#
d = {1:100, 2:200, 3:300, 4:400}
def add_key(d,k,v):
    if k in d:
        d[k] = v
    else:
        d.update({k:v})
add_key(d, 5, 500)
add_key(d, 4, 450)
print(d)

# e. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict1.update(dict2)
dict1.update(dict3)
print(dict1)

# -----------------------------------------------------   Touple   -----------------------------------------------------

# a. Write a Python program to create a tuple with different data types.
#
t = ("tuple", False, 3.2, 1)
print(t)

# b. Write a Python program to create a tuple with numbers and print one item.
#
t = 5, 10, 15, 20, 25
print(t)
t = 5,
print(t)

# c. Write a Python program to add an item in a tuple.
#
t = (4, 6, 2, 8, 3, 1)
print(t)
t = t + (9,)
print(t)
t = t + (15, 20, 25)
print(t)
t = t + t[:len(t)]
print(t)

# d. Write a Python program to convert a tuple to a string.
#
def tuple_to_str(t):
    str = ''
    for item in t:
        str = str + item
    return str
t = ('P','y','t','h','o','n')
str = tuple_to_str(t)
print(str)

# e. Write a Python program to find the length of a tuple.
#
t = tuple("Python")
print(t)
print(len(t))


# -----------------------------------------------------   Sets   -----------------------------------------------------

# a. Write a Python program to add member(s) in a set and clear a set
#
color_set = set()
print(color_set)
print("Add single element:")
color_set.add("Red")
print(color_set)
print("Add multiple items:")
color_set.update(["Blue", "Green"])
print(color_set)

# b. Write a Python program to remove an item from a set if it is present in the set.
#
num_set = set([0, 1, 2, 3, 4, 5])
print("Remove 5 from the said set:")
num_set.discard(5)

# c. Write a Python program to create an intersection, Union, difference of sets.
#
# intersection
a = set([1, 2, 3])
b = set([2, 3, 4])
c = a.intersection(b)
print(c)
# union
a = set([1, 2, 3])
b = set([2, 3, 4])
c = a.union(b)
print(c)
# difference
a = set([1, 2, 3])
b = set([2, 3, 4])
c = a.difference(b)
print(c)

# d. Write a Python program to find maximum and the minimum value in a set.
#
num_set = set([0, 1, 2, 3, 4, 5])
print("Maximum value of the said set:")
print(max(num_set))
print("Minimum value of the said set:")
print(min(num_set))

# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
#
# Lists
listA = [45, 20, 11, 50, 17, 45, 50,13, 45]
print("Given List:\n",listA)
res = max(set(listA), key = listA.count)
print("Element with highest frequency:\n",res)
# 
# Tuples
tupleA = (45, 20, 11, 50, 17, 45, 50,13, 45)
print("Given Touple:\n",tupleA)
res = max(set(tupleA), key = tupleA.count)
print("Element with highest frequency:\n",res)
# 
# Dictionaries
def most_frequent(List):
    return max(set(List), key = List.count)
dict={1:11,2:22,3:33,4:11,5:11}
List = list(dict.values())
a=most_frequent(List)
print(a,List.count(a))