for T in range(int(input())):
    n=int(input())
    d={}
    p={}
    gc={}
    d[-1]=''
    for i in range(n):
        a=list(input().split())
        gd=int(a[1])-int(a[3])
        if gd>=0:
            if(gd in gc):
                gc[gd]+=1
            else:
                gc[gd]=1
            d[gd]=a[0]
    goal=-1
    res=-1
    for i in list(gc.keys()):
        if(goal<gc[i]):
            goal=gc[i]
            res=i
        elif(goal==gc[i]):
            res=max(i,res)
    print(res,d[res])
