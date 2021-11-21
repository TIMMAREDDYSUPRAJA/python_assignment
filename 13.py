a=5
for i in range(a):
	for j in range(0,a-i):
		print(" ",end=' ')
	for k in range(0,i):
		print("*",end=" ")
	print(" ")
for i in range(5,0,-1):
	for j in range(0,5-i):
		print(" ",end=' ')
	for k in range(0,i):
		print("*",end=" ")
	print(" ")
