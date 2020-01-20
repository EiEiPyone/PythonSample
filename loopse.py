loopse.py
>>> x = 1
>>> while x < 7:
...     print(x)
...     x += 1

While loop require variable ready

>>> x = 1
>>> while x < 7:
...     print(x)
...     if x == 5:
...             break
...     x += 1
...


>>> x = 100
>>> x = 10
>>> while x < 100:
...     print(x)
...     if x == 70:
...             break
...     x += 1


#for loops is iterating over a sequence

>>> fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
>>> for x in fruits:
...     print(x)

#Looping in a string
 for x in "pineapple":
...     print(x)

#The break Statement

# stop after condition
>>> fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
>>> for x in fruits:
...     print(x)
...     if x == "pineapple":
...             break

>>> fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
>>> for x in fruits:
...     if x == "pineapple":
...             break
...     print(x)


>>> for x in fruits:
...     if x == "pineapple" and "coconut":
...             break
...     print(x)


>>> for x in fruits:
...     if x == "kiwi":
...             break
...     print(x)



>>> for x in fruits:
...     print(x)
...     if x == "coconut":
...             break
...             print(x)


>>> for x in fruits:
...     if x == "orange":
...             continue
...     print(x)


>>> for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
...     print(x)

>>> for x in range(10):
...     print(x)

>>> for x in range(10, 100):
...     print(x)


>>> for x in range(10,100,5):
...     print(x)
...

>>> NumberA = [1, 2, 3, 4, 5]
>>> NumberB = [1, 2, 3, 4, 5]
>>> for x in NumberA:
...     for y in NumberB:
...             print(x,y)

>> for x in NumberA:
...     print(x,y)

>>> for y in NumberB:
...     print(x,y)



>>> NumberA = [1, 2, 3, 4, 5]
>>> NumberB = [1, 2, 3, 4, 5]
>>> NumberC = [1, 2, 3, 4, 5]
>>> for x in NumberA:
...     for y in NumberB:
...             for z in NumberC:
...                     print(x,y,z)

>>> for x in [1, 2, 3, 4, 5]:
...     pass


>>> words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))



>>> for n in range(2, 10):
...     for x in range(2, n):
...             if n % x == 0:
...                     print(n, 'equals', x, '*', n//x)
...                     break
...     else:
...             print(n,'is a prime number')


>>> for num in range(2, 10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             break
...     print("Found a number", num)
.

>>> for num in range(2, 10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             continue
...     print("Found a number", num)
...
>> name = "Mg Mg"
>>> print('My name is', name)


>>> for num in range(2, 10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             pass
...     print("Found a number", num)













...



...



