values = [1, 2, "yash", 3, 4]   # supports diff data types

print(values[2])    # index 2 is value yash

print(values[-1])   # to print the values in last index, becomes useful when the list is long

print(values[1:4])  # to get a subset of the list [2, "yash", 3]

values.insert(3, "thannir")
print(values)   # [1, 2, 'yash', 'thannir', 3, 4]

values.append('sri')    # to insert something at the end of list use append
print(values)   # [1, 2, 'yash', 'thannir', 3, 4, 'sri']

values[2] = "yashaswi"  # to update a particular value in string
print(values)

del values[0]
print(values)   # [2, 'yashaswi', 'thannir', 3, 4, 'sri']

