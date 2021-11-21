a=16
print("* "*a),;
print("\n")
i=(a//2)-1
j=2
while (i!=0):
	while(j<=(a-2)):
		print("* "*i),;
		print("_ "*j),;
		print("* "*i),;
		print("\n")
		i=i-1
		j=j+2
