# if else condition
greet = "good morning"

if greet == "good morning":
    print("condition matches")
else:
    print("condition does not match")
print("explanation of if else conditional statements")


# for loops

listObj = [1, 2, 3, 4, 5]
# to print all the list values by iteration
for i in listObj:
    print(i)
print("-------------------------")

# to print multiple of 2's for every list vale iteration
for i in listObj:
    print(i*2)
print("-------------------------")

# print sum of first 5 natural numbers
# for i in range(1, 6):  --> range(i, j) i to j-1
sumOfList = 0
for i in listObj:
    sumOfList = sumOfList + i
print(sumOfList)
print("-------------------------")

# range explanation
for k in range(1, 10, 2):
    print(k)
print("-------------------------")

for m in range(10):
    print(m)

print("----while loop----")
# While loops
# can be used to check a condition

i = 10

while i>1:
    if i == 5:
        break   # after coming across break statement it will exit while loop. continue is opp
    if i != 3:
        print(i)
    i = i - 1


