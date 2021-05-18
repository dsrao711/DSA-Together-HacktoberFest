def threeSum(nums):
       
    
    left = 0
    right = len(nums) - 1
    flag = 0
    nums.sort()
    solution = []
    for k in range (0 , len(nums) - 1):
        x = nums[k]
        while(left < right):
            if(nums[left] + nums[right]+x == 0):
                print("bfhbf")
                solution.append([nums[left] , nums[right] , x])
                left += 1
                right -= 1
                flag  = 1
                
            if(nums[left] + nums[right] < x ):
                left += 1
            else:
                right -= 1
    if (flag == 1):
        print(solution)
    else: 
        print([])
              

threeSum([-1,0,1,2,-1,-4])