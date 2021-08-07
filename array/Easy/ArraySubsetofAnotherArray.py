
#https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1#

def isSubset( a1, a2, n, m):
    
    s = set()
    m  = len(a1)
    n  = len(a2)
    
    for i in range(m):
        s.add(a1[i])
        
    p = len(s)
    
    for i in range(n):
        s.add(a2[i])

    if(len(s) == p):
        return 'Yes'
    else:
        return 'No'

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        
        print(isSubset( a1, a2, n, m))

        T -= 1


if __name__ == "__main__":
    main()

