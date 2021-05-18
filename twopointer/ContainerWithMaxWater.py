class Solution:
    def maxArea(self, height: List[int]) -> int:
      
        j = len(height)-1
        i=0
        area = 0
        max_area = 0
        while(True):
            if height[i]<=height[j]:
                area = height[i]*(j-i)
                i+=1
            elif height[i]>height[j]:
                area = height[j]*(j-i)
                j-=1
                
            if area > max_area:
                max_area = area
                
            if i == j:
                return max_area
                break
        
                
            
        