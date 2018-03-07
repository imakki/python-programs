# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(s,t):
	if t in s:
		return s.index(t)
	else:
		return -1

print find_element([1,2,3],3)
print find_element(['alpha','beta'],'gamma')
print find_element(['ankit','akki','rohit'],'ankit')