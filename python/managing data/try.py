# Define a procedure, sum_list,
# that takes as its input a
# list of numbers, and returns
# the sum of all the elements in
# the input list.

p = [1,7,4]

def sum_list(p):
	result = 0
	for e in p:
		result = result + e
	return result

print sum_list(p)