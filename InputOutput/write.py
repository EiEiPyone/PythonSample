# with open('test.txt', 'r') as rf:
# 	with open('testCOPY.txt', 'w') as wf:

# 		for line in rf:
# 			wf.write(line)

with open('jasmine.jpg', 'rb') as rf:
	with open('jasmine_copy.png', 'wb') as wf:

		for line in rf:
			wf.write(line)



