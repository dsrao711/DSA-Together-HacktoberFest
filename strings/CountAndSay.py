# Link : https://leetcode.com/problems/count-and-say/

# Example : 

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"


# Approach : 
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

# Consider the n-1 th string , keep checking the count of each charachter of the string 
# C -> Counter to store the count of each charachter in the string (C = 0)
# ret-> Store the final result string (ret = "")
# S -> stores the n-1th string

# If i-1 and ith element in the string are equal -> Increase the counter
# Else ret = ret + C + s[i-1]


class Solution:
    def countAndSay(self, n):
        if (n == 1):
            return ("1")
        
        s = self.countAndSay(n-1)
        ret = ""
        cnt = 1
        i = 1
        while i < len(s) + 1:
            if i < len(s) and s[i] == s[i-1]:
                cnt += 1
            else:
                ret += str(cnt) + str(s[i-1])
                cnt = 1
            i += 1
            
        return (ret)