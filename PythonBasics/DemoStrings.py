str1 = "this is yashaswi,"
str2 = "how are you?"
str3 = "yashaswi"
str4 = "           heyyyy  "
print(str1[1])   # h
print(str1[0:9])  # this is y
print(str1 + " " + str2)    # this is yashaswi, how are you?
print(str3 in str1)  # substring check - True
print(str2.split(" "))  # ['how', 'are', 'you?']
print(str4.strip())  # removes trailing white spaces from the beginning and end
