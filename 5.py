a=1
z=2
num=z
for i in range(2,6):
	for j in range(a,z):
		num=num-1
		print num,;
	print " "
	a=z
	z=z+i
	num=z
