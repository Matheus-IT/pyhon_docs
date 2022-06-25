# OPENING FILES
# Before a file can be edited, it must be opened, using the open function:
open("filename.txt")

'''
You can specify the mode used to open a file by applying a second argument to the open function:
    Sending "r" means open in read mode, which is the default.
    Sending "w" means write mode, for Rewriting the contents of a file.
    Sending "a" means append mode, for adding new content to the End of the file.
    Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files)

In Python there also exists other modes:
    "r+" - Opens a file for both reading and writing. The file pointer placed at the beginning of the file.
    "w+" - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not
    exist, creates a new file for reading and writing.
    "a+" - Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The 
    file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
It can also be combined with "b"
'''

# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")

'''Once a file has been opened and used, you should close it.
This is done with the close method of the file object'''
file = open("filename.txt", "w")
# do stuff to the file
file.close()

#Abrindo e fechando os arquivos de forma segura:
try:
    file.open('filename.txt', "w+")
    print(file.read())
finally:
    file.close()
