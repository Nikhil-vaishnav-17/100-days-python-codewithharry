#Seek & tell function in File Handling
with open('file.txt', 'r') as f:
    f.seek(5) #Move to the 5th byte of the file

    print(f.read(5)) #Read the next 5 byte
    print(f.tell()) #Tells us on which byte we are on

# f.truncate(5) : removes all the file content after 5 bytes from starting