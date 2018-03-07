# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

p = ['Udacity','Udcious','Umbra']
q = ['Usdf','Udasd','afa','Uafs','Udfas']
def measure_udacity(p):
	count = 0
	for e in p:
		if e[0] == 'U':
			count = count + 1
	return count

print measure_udacity(p)
print measure_udacity(q)
		