from math import sqrt
N=int(input("inserire un intero maggiore di 1: "))
print("i fattori sono:")
a=N
i=2
n=0
while a!=1:
	while a%i==0:
			a/=i
			n+=1
	if n!=0:
		print(i,"con molteplicità",n)
	for i in range(3,N+1,2):
		n=0
		primo=True
		for j in range(3,int(sqrt(i))+1):
			if (i%j)==0:
				primo=False
				break
		if primo:
			n=0
			while a%i==0:
				a/=i
				n+=1
		if n!=0:
			print(i,"con molteplicità",n)
