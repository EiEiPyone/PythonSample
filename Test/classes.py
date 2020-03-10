classes

class Person:
	pass #An empty block

p = Person()	
print(p)


Methods

class Person: #Class
	def say_hi(self): #Function
		print('Hello, how are you?') # syntax

p = Person()
p.say_hi()


__init__ method

class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello,my name is ', self.name)

p = Person('Swaroop')
p.say_hi()

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

	def say_name(self):
		print('Hello,my name is ', self.name)

	def say_age(self):
		print('I am',self.age, 'years old.')

	def say_name_age(self):
		print('My name is', self.name,'.I am',self.age, 'years old.')

p = Person('U Ba', '30')
p.say_name()
p.say_age()
p.say_name_age()

q = Person('Daw Mya', '45')
q.say_name()
q.say_age()
q.say_name_age()






dog = dog('Name')
dog.color('Black')
dog.owner('U Kaung')


dog.function() - bark
			   - eat
			   - sleep
			   - bite 

-------------------------------

#Class And Object Variables

class Robot:
	"""Represents a robot,with a name."""

	population = 0

	def __init__(self,name):
		"""Initializes the data."""

		self.name = name
		print("(Initializing{})".format(self.name))

		Robot.population += 1

	def die(self):
		"""I am dying."""

		print("{} is being destroyed!".format(self.name))

		Robot.population -= 1

		if Robot.population == 0:
			print("{} was the last one.".format(self.name))
		else:
			print("There are still {:d} robots working.".format(
				Robot.population))	

	def say_hi(self):
		""""Greeting by the robot.	
		Yeah, they can do that."""		

		print("Greetings, my sisters call me{}.".format(self.name))


	@classmethod
	def how_many(cls):
			"""Prints the current population."""
			print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot ("C-3PO")
droid2.say_hi()
Robot.how_many()

droid3 = Robot("Q35")
droid3.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work.so let's destory them")
droid1.die()
droid2.die()
droid3.die()

Robot.how_many()	


#Inheritance


class SchoolMember:
	'''Represents any school member.'''

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Initialized ShcoolMember: {})'.format(self.name))


	def tell(self):
		'''Tell my details.'''
		print('Name:"{}" Age:"{}"'.format(self.name, self.age),end="")


class Teacher(SchoolMember):
	'''Represents a student.'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Initialized Student:{})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))


class Student(SchoolMember):
	'''Represents a Student'''

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized Student:{}'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: "{:d}"'.format(self.marks))	



t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)


print()


members =[t,s]
for member in members:
	membr.tell()		