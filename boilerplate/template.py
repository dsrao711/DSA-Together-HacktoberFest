
class Solution:
    def dummy(n,r):
        return n + r
        

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.dummy(n, r))
