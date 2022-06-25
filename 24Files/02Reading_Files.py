# Reading Files
# The contents of a file that has been opened in text mode can be read using the read method
file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

'''To read only a certain amount of a file, you can provide a number as an argument to the read function. This 
determines the number of bytes that should be read.
You can make more calls to read on the same file object to read more of the file byte by byte. With no argument, 
read returns the rest of the file. '''
file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read())
file.close()

'''To retrieve each line in a file, you can use the readlines method to return a list in which each element is a
line in the file.
For example:'''
file = open("filename.txt", "r")
print(file.readlines())
file.close()
#Result:
#>>>
#['Line 1 text \n', 'Line 2 text \n', 'Line 3 text']
#>>>
'''You can also use a for loop to iterate through the lines in the file: '''
file = open("filename.txt", "r")
for line in file:
    print(line)
file.close()
#Result:
#>>>
#Line 1 text
#Line 2 text
#Line 3 text
#>>>
