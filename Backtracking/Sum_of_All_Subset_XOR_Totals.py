'''
question link- https://leetcode.com/problems/sum-of-all-subset-xor-totals/


Sum of All Subset XOR Totals
Question statement:
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
'''

def subsetXORSum(self, nums):
        
        l = len(nums)
        res = 0

        stack = [(0, 0)]

        while stack:
            pos, xor = stack.pop()
            res+=xor
            for i in range(pos, l):
                stack.append((i+1, xor^nums[i]))
        return res
