# tuples are immutable - it cannot be updated. It is protected.
# lists are mutable - updates are allowed.

tupleDemo = (1, 2, "yash", 4, 5)
print(tupleDemo)

# tupleDemo[2] = "yashaswi" --- TypeError: 'tuple' object does not support item assignment
# print(tupleDemo)

# dictionary

dict1 = {"a": 1, 2: "bcd", 3: "efg"}
print(dict1)    # {'a': 1, 2: 'bcd', 3: 'efg'}

print(dict1["a"])   # 1
print(dict1[2]) # bcd

# how to create dictionaries dynamically at run time
dict2 = {}
dict2["firstname"] = "yashaswi"
dict2["lastname"] = "thannir"
dict2[3] = "FullNameField"

print(dict2)    # {'firstname': 'yashaswi', 'lastname': 'thannir', 3: 'FullNameField'}


