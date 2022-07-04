# Approach 1 : Using max heap 
# TC : O(n + klogn)

import heapq
class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)  # create a min-heap whose size is k 
        for num in nums[k:]:
            if num > heap[0]:
               heapq.heapreplace(heap, num)
            # or use:
            # heapq.heappushpop(heap, num)
        return heap[0]

#https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# TC : O(n)
class Solution:
    def findKthLargest(self, nums, k):
        n = len(nums)
        k = n - k 
        def QuickSelect(l , r):
            # First and last index as Pointer p and Pivot element
            pivot , p = nums[r] , l 
            for i in range(l , r):
                # IF curr element less than pivot , keep it as it and upgrade pointer p
                if(nums[i] <= pivot):
                    nums[p] , nums[i] = nums[i] , nums[p]
                    p += 1
            # Swap the pointer p's element with Pivot
            nums[p] , nums[r] = nums[r] , nums[p]
            # Now the the pointer p is at a position where items to the left of it are smaller than the pivot and to the right are greater than pivot 
            # Obv , we are interested in the largest element so we check that
            
            if(p < k) :
                # Sort the right half 
                return QuickSelect(p+1 , r)
            elif(p > k):
                # Sort the left half
                return QuickSelect(l , p-1)
            else:
                return nums[p]
        op = QuickSelect(0 , n - 1)
        return op
                    