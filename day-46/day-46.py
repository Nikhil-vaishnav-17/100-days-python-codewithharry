#Use of 'os' module

"""
You can create, delete, rename file or directories in the system.
You can also make the cmd to open up and run the file
"""
import os

"""
cmd ='date'
os.system(cmd) #Run the 'date' cmd in terminal
"""

print(os.getcwd()) #Print the working directory

"""
Their are many functions in the os module you can search it on google for more
"""

for func in dir(os):
    print(func)