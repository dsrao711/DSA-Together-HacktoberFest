# https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/

def SplitBinaryString(s , n):
    
    count_0 = 0
    count_1 = 0 
    
    counter = 0
    
    for i in range(n):
        if(s[i] == '0'):
            count_0 += 1
        else:
            count_1 += 1
            
        if (count_0 == count_1):
            counter += 1
    
    if count_0 != count_1 :
        return -1
            
    return counter

#Driver Code

a ="010100110011"

size = len(a)

op = SplitBinaryString(a, size)

print(op)