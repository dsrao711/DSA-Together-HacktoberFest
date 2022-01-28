# https://ibb.co/JHjWxss
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        dp = [0]*n
    
        
        for i in range(0 , n):
            if(i == 0):
                dp[i] = 1
            print(s[i])
            if(s[i-1] == 0 and s[i] == 0):
                print(s[i-1] + s[i])
                dp[i] = 0
                
            elif(s[i-1] != 0 and s[i] == 0):
                print(s[i-1] + s[i])
                if(int(s[i-1] + s[i]) <= 26):
                    if (i >= 2):
                        dp[i] = dp[i-2]
                    else:
                        dp[i] = 1     
                else:
                    dp[i] = 0
                        
            elif(s[i-1] == 0 and s[i] != 0):
                print(s[i-1] + s[i])
                dp[i] = dp[i-1]
                
            else :
                if(int(s[i] + s[i-1]) <= 26):
                    print(s[i] + s[i-1])
                    if (i >= 2):
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1] 
            
            print(dp)
            
            return dp[-1]
                    
                
            