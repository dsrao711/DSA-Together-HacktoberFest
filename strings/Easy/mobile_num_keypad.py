# https://www.geeksforgeeks.org/convert-sentence-equivalent-mobile-numeric-keypad-sequence/

# Python3 implementation to convert
# a sentence into its equivalent
# mobile numeric keypad sequence

def printSequence(arr, input):

# length of input string
	n = len(input)
	output = ""
	
	for i in range(n):
		if(input[i] == ' '):
			output = output + "0"
		else:	
			position = ord(input[i]) - ord('A')
			output = output + arr[position]
	return output
	
# Driver code
str = ["2", "22", "222",
	"3", "33", "333",
	"4", "44", "444",
	"5", "55", "555",
	"6", "66", "666",
	"7", "77", "777", "7777",
	"8", "88", "888",
	"9", "99", "999", "9999" ]

input = "HELLOWORLDLETSDODSA";
print( printSequence(str, input))

