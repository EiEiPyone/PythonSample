function.py
#Global Statement

def func():
	global x

	print('x is' ,x)
	x = 2
	print('Change global x to' ,x)

x = 50
func()
print('Value of x is' , x )

#Default Argument Values in Functions

def say(message, times=1):	
	print(message * times )

say('Hello')
say('World', 5 )
say('Good Bye')
	