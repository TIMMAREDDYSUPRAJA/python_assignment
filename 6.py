def tri_fun(size):
	for i in range(0,size):
		for j in range(0,i+1):
			print fun(i,j),;
		print("")
def fun(a,b):
	num=1
	if b>a-b:
		b=a-b
	for i in range(0,b):
		num=num*(a-i)
		num=num//(i+1)
	return num
ran=7
tri_fun(ran)
