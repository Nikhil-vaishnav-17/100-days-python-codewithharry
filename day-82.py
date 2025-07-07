#Shoutout to everyone
import subprocess

L = ['Rahul', 'Nikhil', 'Himanshu']
print("Shoutout started")
for item in L:
    subprocess.run(['say', f'Shout out to {item}'])
print("All shout out is done")

"""
from os import system

L = ['Rahul', 'Nikhil', 'Himanshu']
print("Shoutout started")
for item in L:
    system(f'say Shout out to {item}')
print("All shout out is done")
"""