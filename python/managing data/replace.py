# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

spy = [0,0,7]
def replace_spy(p):
	p[2] = p[2] + 1

replace_spy(spy)
print spy 