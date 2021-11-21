b=2*6-2
for i in range(6,-1,-1):
	for j in range(b,0,-1):
		print("",end=" ")
	b=b+1
	for j in range(0,i+1):
		print ("*",end=" ")
	print(" ")
