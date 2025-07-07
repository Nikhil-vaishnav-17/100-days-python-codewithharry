#File handling

#Reading the file
f = open('my_file.txt', 'r') #Opens the file in read mode we can remove the 'r' as it is read mode in default

text = f.read()
print(text)
f.close()

"""
'w' : used to open the file in write mode, it will create the file if it does not exist

'a' : opens the file in append mode

'rb' : opens the file in binary mode useful when opening a .jpg file or any other file

"""

#Writing in a file
f = open('write_file.txt', 'w')
f.write('Hello world')
f.close()

#You can use 'with' keyword to open the file
with open('write_file.txt', 'a') as f:
    f.write("\nThis is a new line")