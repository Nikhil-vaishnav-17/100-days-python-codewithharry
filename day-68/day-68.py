#Change the name of files
import os

def change_file_names(type_of_file:str):
    directory = 'files/'
    counter = 1
    for filename in os.listdir(directory):
        if filename.endswith(f'.{type_of_file}'):
            old_name = f'{directory}{filename}'
            new_filename = f'{directory}{type_of_file}_{counter}.{type_of_file}'

            os.rename(old_name, new_filename)
            counter += 1

user_input = input("Enter the type of file you want to change the name: ")
change_file_names(user_input)

print(f'Changed every {user_input} name if present')