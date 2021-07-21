def removeDuplicates(nums):
    n = len(nums)
    mp = {}
    for i in range(0 , n):
        if nums[i] not in mp:
            mp[nums[i]] = nums[i]
        
    op = mp.keys()
    return op

op = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(op)
