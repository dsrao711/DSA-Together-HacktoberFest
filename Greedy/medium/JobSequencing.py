# Problem : https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        l = []
        for job in Jobs:
            l.append([job.profit , job.deadline])
            
    
        l.sort(key = lambda x : x[1])
        l.sort(key = lambda x : x[0] , reverse = True)
      
        
        results = [False]*n
        profit = 0
        counter = 0
        
        for i in range(0 , n):
            for j in range(min(n-1 , l[i][1] - 1) , -1 , -1):
                if(results[j] == False):
                    counter += 1
                    profit += l[i][0]
                    results[j] = True
                    break
                
        return ([counter , profit])
                    
                
        
# Driver Code

import atexit
import io
import sys


class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
