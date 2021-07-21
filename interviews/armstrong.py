# python3 >= 3.6 for typehint support
# This example avoids the complexity of ordering
# through type conversions & string manipulation

def isArmstrong(val:int) -> bool:
	
	
	parts = [int(_) for _ in str(val)]
	
	# begin test.
	counter = 0
	for _ in parts:
		counter += _**3
	return ( counter == val )

print(isArmstrong(100))

print(isArmstrong(153))

# Get all the Armstrong number in range(1000)
print([ _ for _ in range(1000) if isArmstrong(_)])
