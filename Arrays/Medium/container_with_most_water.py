def maxArea(height) -> int:
    maxArea = 0
    l = 0
    r = len(height)-1
    while (l < r):
        maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
        if (height[l] < height[r]):
            l+=1
        else:
            r-=1
    return maxArea

if __name__ == "__main__":
    height = list(map(int, input().strip().split(" ")))
    print(maxArea(height))