#Class and objects

class Person:
    name, occupation = str(), str()
    networth = int()
    def info(self):
        print(f'{self.name} is a {self.occupation} & have a net worth of {self.networth}')

a = Person()
b = Person()

a.name, a.occupation, a.networth = 'Nikhil', 'Software developer', 1000
b.name, b.occupation, b.networth = 'Neeraj', 'Full stack developer', 2000

a.info()
b.info()