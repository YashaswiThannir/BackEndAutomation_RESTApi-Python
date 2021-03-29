fileObj = open('text')
#print(fileObj.read()) # prints all lines, line by line
#print(fileObj.read(2)) # prints the first two line in the file
#print(fileObj.readline()) # prints sinle line
#print(fileObj.readline())
#fileObj.close()

# program to read line by line using readLine method
#line = fileObj.readline()
#while line != "":
#    print(line)
#    line = fileObj.readline()

lines = fileObj.readlines()  # arranges all the lines in the form list
for l in lines:
    print(l)
print(lines[3])
fileObj.close()

with open('text', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text', 'w') as writer:
        for line in reversed(content):
            writer.write(line)