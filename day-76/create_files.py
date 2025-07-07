import random
import string

def create_files(type_of_file:str, no_of_files:int):
    directory = 'files/'
    for _ in range(no_of_files):
        filename = ''.join(random.choices(string.ascii_letters + string.digits , k=8)) + f'.{type_of_file}'
        file_path = f'{directory}{filename}'
        with open(file_path, 'wb') as f:
            f.write(b'')

file_type = input("Enter the type of file you want to create: ")
no_of_file = int(input('How many files you want to create: '))
create_files(file_type,no_of_file)

print(f"Created {no_of_file} {file_type} successfully")