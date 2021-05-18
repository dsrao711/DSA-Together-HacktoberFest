
def threeSum(nums):

  res = set()
  nums.sort()
  for i in range(len(nums)-2):

    target = -(nums[i])
    left = i + 1
    right = len(nums)-1
    
    while left < right:
      sum = nums[left] + nums[right]
      if sum == target:
        res.add((nums[i],nums[left],nums[right]))
        left += 1
      elif sum < target:
        left += 1
      else:
        right -= 1
        
  print(list(res)) 

            

arr = [-1,0,1,2,-1,-4]
threeSum(arr)


# Find a pair of nums whose sum is equal to -ve value of a number in the list so that the sum of all three nums is 0