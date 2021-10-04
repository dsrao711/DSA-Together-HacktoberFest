# Program to check if strings are rotations of of each other or not

def areRotations(string1, string2):
	return (len(string1) == len(string2) and string2 in string1 + string1)

# Driver code
string1 = "AACD"
string2 = "ACDA"

if areRotations(string1, string2):
	print( "Strings are rotations of each other")
else:
	print ("Strings are not rotations of each other")

