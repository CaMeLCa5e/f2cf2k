# Fahrenheit to celsius 

def f2c (f):
	c = (5.0/9) * (f-32)
	return c
x1 = f2c (32)
x2 = f2c (212)

print x1, x2
print ''
print 'Kelvin-' 
print ''

#F2Kelvin 

def f2k(f):
	c= f2c(f)
	k = c + 273.15
	return k
	
k1 = f2k(32)
k2 = f2k(212)

print k1, k2
