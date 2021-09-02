#https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/


# Problem statement : 

# We need to return the number of steps to make the frequency of elements unique
# No two elements should have the same frequency 
# Basically we can get the count of each element by storing it in a dict
# Sinc a set has all the elements which are unqiue
# So we can add the freq of the elements from the dict to the set 


# Approach :

# Variables : 
# counter  => number of step required to make the frequency of the elements unique
# 1. Using counter from collections , we can store the count of  each element in the dict 
# S = {a : 3 , b : 2 , c : 2 , e : 1}
# Create an empty set unique = () to store the unique frequencies

# for char ,  freq in S.items():
#   while( freq > 0 and freq in unique):
#       freq -= 1
#       counter += 1

#   unique.add(freq)


# First iteration : 
# freq = 3 , freq > 0 and freq in unique = F 
# unique = (3) , counter = 0 , freq = 3

# Second iteration : 
# freq = 2 , freq > 0 and fref in unique = F
# unique = (3 , 2 ) , counter = 0 , freq = 2

# Third iteration
# freq = 2 , freq > 0 and freq in unique = T
# freq -- => freq = 1 , counter ++ => counter = 1
# freq = 1 , freq > 0 , freq in unique = F 
#unique(3,2,1) , counter = 1 , freq = 1

# Fourth iteration 
# freq = 1 , freq > 0 and freq in unique = T
# freq-- , freq = 0 , counter = 2 
# unique = (3,2,1,0)



from collections import Counter

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        S = Counter(s)
        count= 0
        unique = set()

        for char, freq in S.items():
          
            while freq >0 and freq in unique:
                freq-=1
                count+=1
            unique.add(freq)

        return count