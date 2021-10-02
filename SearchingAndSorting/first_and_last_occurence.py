#Link : https://practice.geeksforgeeks.org/viewSol.php?subId=4c93efc2627e9e47ceb06b5f1aaa5d03&pid=703459&user=divyarao1

def find(arr,n,x):
    arr.sort()
    op = []
    for i in range(0 , n) :
        if arr[i] == x :
            op.append(i)
            break
    rev = arr[::-1]
    for i in range (0 , n):
        if (rev[i] == x):
            op.append(n - i - 1)
            break
        
    if(len(op) == 0):
        return [-1 , -1]
    return op
                 
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
