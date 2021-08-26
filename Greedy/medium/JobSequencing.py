# Problem : https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
# Referred : https://www.youtube.com/watch?v=bID397v7ja4&t=600s

# Note: 

# Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job.
# Each job takes 1 unit of time

# Input 1:
# N = 4
# Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
# Output:
# 2 60
# Explanation:
# Job1 and Job3 can be done with
# maximum profit of 60 (20+40).

# Input 2 :

# N = 5
# Jobs = {(1,2,100),(2,1,19),(3,2,27),
#         (4,1,25),(5,1,15)}
# Output:
# 2 127
# Explanation:
# 2 jobs can be done with
# maximum profit of 127 (100+27).


# Problem statement

# We are supposed to return the maximum profit here 
# There would be many jobs that can be performed in the deadline 1 , but we need to choose that job
# which gives more profit in order to maximize the profit
# So our criteria for selecting a job should be profit and then we need to check if we can finish 
# this job in the given deadline
# Sorting the array on the basis of profit -> [40,1] , [30,1] , [20,4] , [10,1]


# Now consider the second example , both the jobs are of deadline 2 but still we could perform both

# Reason being -> Each job takes one unit of time , so for a job with deadline 2 , we can perform 
# that job at unit time 1 or 2 . 
# Our approach would be to check whether the job with dealine 2 can be performed at unit time 2 or not ?
# If yes , then we perform it at 2 leaving the other time slots for other jobs to maximise o/p
# If no , then we keep on checking till first index i.e unit time 1 here and allot the previous time slot
# before 2

# Since each job takes 1 unit of time , and since there are 4 jobs we create a list of deadlines
# deadlines = [False , False , False , False] 
# False indicates empty slot

# So basically if a job has deadline x , we need to check if the deadlines list has any slot empty 
# from index x - 1 to 0 

#(We do x - 1 because the list follows 0 indexing)

# As soon as a job occupies a time slot from x-1 to 0 , the time slot get updated to T in the deadlines list , so
# that no other job can be performed in that slot


# Variables : 

# deadlines = [False]*n
# counter => No of jobs that can be performed . counter = 0
# profit => Total profit . profit = 0

# Steps
# Consider x => job.deadline
#1. Sort the jobs in descending order of profits
#2. for i in jobs:
# 		for j in (min(n , x-1) , -1):
#			counter ++
#			profit += job.profit

# We did min(n , x-1) so that even if the deadline is more than n , the list doesnt go out of range
#3. return counter , profit

# Code : 
# TC : O(n^2)
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
		
        l = []
        # Storing the Job Profit and Job deadlines in a list
        for job in Jobs:
            l.append([job.profit , job.deadline])
            
        # Sorting the job in descending order of profits
        l.sort(key = lambda x : x[1])
        l.sort(key = lambda x : x[0] , reverse = True)
      

        deadlines = [False]*n
        profit = 0
        counter = 0
        
        for i in range(0 , n):
            for j in range(min(n-1 , l[i][1] - 1) , -1 , -1):
                # If a slot if free , Job can be performed
                if(deadlines[j] == False):
                    counter += 1
                    profit += l[i][0]
                    deadlines[j] = True
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
