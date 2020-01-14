If_Else_Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))

Python Conditions

Equals                   -> x == y
Not Equals               -> x != y
Less than                -> x <  y
Less than or equal to    -> x <= y
Grater than              -> x >  y
Greater than or equal to -> x >= y
Boolean OR               -> x or y , x | y
Boolean AND              -> x and y, x & y
Boolean NOT              -> not x

if -
else -
>>> x = 10
>>> if x == 0:
...     print ("Hello")
... elif x != 0:
...     print("World")
... elif x >= 20:
...     print ( "x is 20")
... else:
...     print("x is 10")

 x = 10
>>> if x == 0:
...     print("Hello")
... elif x != 0:
...     print("world")
... elif x >= 20:
...     print("x is 20")
... elif x == 10:
...     print("x is 10")
... else:
...     print("x is nothing")


x = 10
>>> if x== 0:
...     print("x is zero")
... elif x != 0:
...     print("x is equal zero")
... elif x < 20:
...     print("x is 20")
... elif x == 10:
...     print("x is 10")
... else:
...     print("x is nothing")


>>> x = 70
>>> y = 60
>>>
>>> if x < y:
...     print("x is grater than y")
...
>>> x = 50
>>> y = 150
>>> if x > y:
...     print("x is greater than y")
... elif x == y:
...     print("x and y are equal")
... else:
...     print("x is less than y")

#Short Hand If
 if x > y: print("x is greater than y")

 x is less than y
>>> if x > y: print("x is greater than y")
...
>>>
>>> if x < y: print("x is greater than y")
...
x is greater than y
>>> print("")



>>> x = 50
>>> y = 150
>>> print(x) if x > y else print (y)

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y or z < y:
...     print("one of the conditions is True")
... elif x > y and z > y:
...     print("All conditions are True")
... else:
...     print("nothing else")



>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y and x > z:
...     print("All Conditions are True")
... else:
...     print("one condition is True")


>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y or x > z:
...     print("All Conditions are True")
... else:
...     print("one conditions is True")
...
All Conditions are True
>>>

>>> x = 50
>>> y = 40
>>> z = 100
>>> if x > y and z > y or x > z:
...     print("All Conditions are True")
... else:
...     print("one condition is True")
...
All Conditions are True



>>> x = 50
>>>
>>> if x > 10:
...     print("x is ten")
...     if x > 20:
...             print("x is greater than 20")
...     else:
...             print("No,x is not greater than 20")
...
x is ten
x is greater than 20


>>> if x < 10:
...     print("x is ten")
...     if x > 20:
...             print("x is greater than 20")
...     else:
...             print("No,x is not greater than 20")
... else:
...     print("x is 50")
...
x is 50


>>> x = 100
>>> y = 50
>>> if x > y:
...     pass


int(input("Examination Result : "))
100 - 90       - A
90  - 70       - B
70  - 60       - C
60  - 40       - D
40  - 10       - Fail

>>> Loops

if x >= 70 and x < 90 :
		print("Grade B")