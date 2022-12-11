# 1. Write a python program to create and print a dictionary which stores your information. (name, age, gender .....)

d = {'name': 'aniket', 'age': '21', 'gender': 'male', 'DOB': '16-03-2001'}

print(d)

# 2. Write a python program to access the items of a dictionary by referring to its key name.
d = {'name': 'aniket', 'age': '21', 'gender': 'male', 'DOB': '16-03-2001'}
print()
print(d, end='\n\n')
print('Name :', d['name'])
print('Age :', d['age'])
print('Gender :', d['gender'])
print('Date of birth :', d['DOB'])

# 3. Write a python program to get a list of the values from a dictionary.
d = {'name': 'aniket', 'age': '21', 'gender': 'male', 'DOB': '16-03-2001'}

value_list = d.values()

print(value_list)

# 4. Write a python program to change the value of a specific item by referring to its key name.
d = {'name': 'aniket', 'age': '21', 'gender': 'male', 'DOB': '16-03-2001', 'class': 'SY B-Tech'}

print(d)
print()
d['class'] = 'TY B-Tech'
print(d)

# 5. Write a python program to print all key names in the dictionary, one by one.

d = {'name': 'aniket', 'age': '21', 'gender': 'male', 'DOB': '16-03-2001', 'class': 'SY B-Tech'}

for k in d.keys():
    print(k)


# 6. Write a python program to create a dictionary that contains three dictionaries. (nested)

d1 = {'A': {'B': {'C': 'D'}}}


# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'A': 110, 'B': 210, 'C': 310}
d3 = {'name': 'abc', 'works_at': 'xyz_company'}

d4 = {1: d1, 2: d2, 3: d3}

print(d4)

# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'A': 110, 'B': 210, 'C': 310}
d3 = {'name': 'abc', 'works_at': 'xyz_company'}

d4 = {1: d1, 2: d2, 3: d3}

print(d4)

# 7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'A': 110, 'B': 210, 'C': 310}
d3 = {'name': 'abc', 'works_at': 'xyz_company'}

d4 = {1: d1, 2: d2, 3: d3}

print(d4)

# 8. Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.

l1 = [1, 2, 3, 4]
l2 = ['Aniket', 'Prathmesh', 'Akshay', 'Nishant']
d = {}

for i in range(len(l1)):
    d[l1[i]] = l2[i]

print(d)

# 9. Write a python program to merge two python dictionaries into one dictionary.
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'A': 110, 'B': 210, 'C': 310}

for k, v in d2.items():
    d1[k] = v


print(d1)

# 10. Write a python program to get the key of lowest value from the dictionary.
# sample_dict = {
# 'C': 92,
# 'Java': 66,
# 'Python': 85
# }

sample_dict = {'C': 92, 'Java': 66, 'Python': 85}

print(min(sample_dict.values()))

value = min(sample_dict.values())

for k, v in sample_dict.items():
    if v == value:
        print(k, 'has minimum value', v)
        break