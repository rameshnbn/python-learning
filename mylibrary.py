def add(a,b):
	return a+b
	
def sqr(a):
	return a*a
	
def isPrime(x):
	if x==1: return False
	sq=int(x**0.5)
	for i in range(2,sq):
		if x%i==0: return False
	return True
