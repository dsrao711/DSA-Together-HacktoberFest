# https://www.geeksforgeeks.org/nuts-bolts-problem-lock-key-problem-set-2-hashmap/

class Solution:
    
    def matchPairs(self,nuts, bolts, n):
        # code here
        order = '!#$%&*@^~'
        nut_hash = {}
        
        for i in range(0 , len(nuts)):
            nut_hash[nuts[i]] = i
 
        j = 0
        for i in range(len(order)):  
            if order[i] in nut_hash:  
                nuts[j] = order[i]
                bolts[j] = order[i]
                j += 1
               

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

