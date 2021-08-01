# https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/

def maxSubsString(x):
    count = 0
    count_0 = 0
    count_1 = 0
    n = len(x)
    for i in range(0 , n):
        if(x[i] == 0):
            count_0 += 1
        if(x[i] == 1):
            count_1 += 1
        if(count_0 == count_1):
            count += 1
            
        if(count == 0):
            return -1
        else:
            return count
   

binary_string = input()
op = maxSubsString(binary_string)
print(op)