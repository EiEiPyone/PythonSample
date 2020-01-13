set&Dictionary.py
Sets
includes a data type for sets.



basket = {'apple, 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                          # unique letters in a
a - b                      # letters in a but not in b
a | b                      # letters in a or b or both
a & b                      # letters in both a and b
a ^ b                      # letters in a or b but 

a = {x for x in 'abracadabra' if x not in 'abc'}

fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
print("cherry" in fruits)

fruits.add("cucumber")
fruits
fruits.update("grape") x
fruits
fruits.remove("banana")
fruits
fruits.discard("kiwi")
fruits

>>>Dictionaries

#Dictionaries

#Another useful data type built into Python is the dictionary

tel = {'jack': 4098, 'sape': 4139}
tel['sape']
tel['guido'] = 4127
tel

del tel['sape']
tel['irv'] = 4137
tel

list(tel)    # Change to List
sorted(tel)  #Alphabet Sorting

'guido' in tel
'jack' not in tel

dict(sape=4139, guido=4127, jack=4098)
{x: x**2 for x in (2, 4, 6)}

for x in 2, 4, 6:
	print(x: x**2)
2 : 4
4 : 16
6 : 36

{x: x**3 for x in (1, 2, 3, 4, 5)}

1 : 1
2 : 8
3 : 27
4 : 64
5 : 125

#When looping through dictionaries

knights = {'gallahad' : 'the pure', 'robin' : 'the brave' }
for k,v in knights.items():
	print(k,v)	
for i,v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)	
questions = ['name', 'quest', 'favourite color' ]
answers = ['lancelot', 'the holy grail', 'blue']
result = ['1','2','3']
for q, a, i in zip(questions, answers, result):
print('{0} and {1} , {2} and {3}'.format('spam', 'eggs', 'color', 'food'))