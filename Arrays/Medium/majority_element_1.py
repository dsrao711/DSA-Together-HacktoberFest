"""
Majority element - 1 
Link to the problem : https://leetcode.com/problems/majority-element/
Refer : https://youtu.be/X0G5jEcvroo

"""


"""
T.C : O(n^2)
S.C : O(1)
Brute Force Approach

Store the max of the nums in a variable 'max_so_far'
Find the count of each element and update the 'max_so_far' accordingly 
"""
# Code here

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = 0
        majority_element = -1

        for i in range(0, len(nums)):
            current_element_count = 0

            for j in range(0, len(nums)):
                if nums[j] == nums[i]:
                    current_element_count += 1

            if max_so_far < current_element_count:
                max_so_far = current_element_count
                majority_element = nums[i]

        return majority_element


"""
T.C : O(nlog(n))
S.C : O(1)
Sorting approach

Optimizing the above approach
Sort the nums 
Count the freq till the elements are matching and store the count in 'max_so_far'
Keep repeating the process for rest of the elements and update the max_so_far
Return max_so_far
"""
# Code here

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_so_far = -1
        majority_element = -1
        current_index = 0

        while current_index < len(nums):
            tmp_index = current_index
            current_element_count = 0
            # keep traversing all elements equal to current element and increment the count
            while tmp_index < len(nums) and nums[tmp_index] == nums[current_index]:
                current_element_count += 1
                tmp_index += 1

            if max_so_far < current_element_count:
                max_so_far = current_element_count
                majority_element = nums[current_index]
            current_index = tmp_index

        return majority_element

"""
T.C : O(n)
S.C : O(n)
Hashmap approach 

Use an extra space by taking a hashmap 
Store the count of each element in the hashmap
Return the element with the max count in the hashmap

"""
# Code here

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element = -1
        majority_element_count = 0

        # Hashmap to store element count in the list
        element_frequency_map = {}

        for i in range(0, len(nums)):
            current_element_count = element_frequency_map[nums[i]]
            current_element_count += 1
            # check if current element is majority element
            if majority_element_count < current_element_count:
                majority_element_count = current_element_count
                majority_element = nums[i]
            element_frequency_map[nums[i]] = current_element_count

        return majority_element

"""
Best approach
T.C = O(n)
S.C = O(1)
Moore's Voting Algorithm - Google interview question
"""
# Code

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize ans_index as first element 
        ans_index = 0
        counter = 0
        n = len(nums)

        for i in range(0 , n):
            # Check if the ans_index is equal to array element , if yes , increase the counter or else reduce it
            if(nums[i] == nums[ans_index]):
                counter += 1
            else:
                counter -= 1
            # If counter is zero , we need to change the ans_index
            if(counter == 0):
                ans_index = i
                counter = 1
        # Confirm if the result of this algorithm is correct by finding the frequency of this element
        freq = 0
        res = -1

        for i in range(0 , n):
            if(nums[i] == nums[ans_index]):
                freq += 1
        # If the freq is greater than n/2 , it satisfies our condition
        if(freq >= (n/2)):
            res = nums[ans_index]

        return res
