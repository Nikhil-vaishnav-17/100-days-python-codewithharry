class Person:
    name, occupation = str, str
    networth = int

    def __init__(self, name = '', occupation = '', networth = 0):
        self.name = name
        self.occupation = occupation
        self.networth = networth

    def info(self):
        print(f'{self.name} is a {self.occupation} & have a net worth of {self.networth}')

a = Person('Nikhil', 'Software developer', 1000)
b = Person('Neeraj', 'Full stack developer', 2000)
c = Person()

a.info()
b.info()
c.info()