#Link to Problem : https://leetcode.com/problems/super-ugly-number/

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        i = 1
        a = []
        
        # a is a min-heap of list that stores [prime,0,prime] for each element in the given list of primes 
        for prime in primes:
            a.append([prime,0,prime])
        
        #ugly is the list that will be storing first n super ugly numbers
        # 1 is a first super ugly number 
        ugly = [1]
        
        while(i < n):
            x = a[0][0] #x is the min element in a
            ugly.append(x)
            
            while a[0][0] == x: #till min element in heap equals x
                cur = heapq.heappop(a) #remove the min element from heap
                cur[1] += 1
                cur[0] = ugly[cur[1]]*cur[2]
                heapq.heappush(a,cur) #insert cur in heap
            i += 1    
        
        #return the last ugly number
        return ugly[n-1]

#Time Complexity : O(NK*log(K)) where K is the number of primes