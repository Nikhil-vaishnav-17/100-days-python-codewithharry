#F string
txt = "My name is {}, i am from {}"
name = 'Nikhil'
country = 'India'

print(txt.format(name,country)) #Puts the name in the first {} bracket and country in second

#You can also specify which will belongs to which by the number
txt = "My name is {1}, i am from {0}"
name = 'Nikhil'
country = 'India'

print(txt.format(country,name)) #name = 1 & country = 0

#This is not at all a better way so we use f-string
#you can directly create an f string by putting an f before the string and you can use variables in the string

txt = f"My name is {name}, my country is {country}"
print(txt)

#You can print an f-string with curly brackets as it is by just replacing the single brackets with double
txt = f"My name is {{name}}, my country is {{country}}"
print(txt)