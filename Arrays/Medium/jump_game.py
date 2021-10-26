 '''
 Link - https://leetcode.com/problems/jump-game

 Difficulty - Medium

  O(n)
 '''
class Solution:
	def canJump(self, nums: List[int]) -> bool:
		last_position = len(nums)-1
			
		for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
			if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
				last_position = i # Since we just need to reach to this new index
		return last_position == 0	