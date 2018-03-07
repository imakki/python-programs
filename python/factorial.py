# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    result = 1
    while n >= 1:
    		result = result * n
    		n = n-1
    return result
print factorial(4)
		