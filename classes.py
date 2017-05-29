class Person:
  title = "undefined"
  def __init__(self, name, job):
    self.name = name
    self.job = job
  def talk(self):
    print("Hello, I'm %s, and my job is %s" %(self.name, self.job))

class Doctor(Person):
  title = "Dr"
  def talk(self):
    print("Hello, I'm %s %s, and my job is %s" %(self.title, self.name, self.job))  

chandler = Person('Chandler', 'Changing tabs to space')
chandler.talk()
print(chandler.title)

print('-----------------')

janet = Doctor('Janet', 'curing people')
janet.talk()
print(janet.title)


