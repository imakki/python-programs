# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
	if day == 'Saturday'or day == 'Sunday':
		return True
	else:
		return False

print weekend('Saturday')
print weekend('Monday')
print weekend('July')
