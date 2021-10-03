def pattern(n):
    k = 2*n - 2
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")
        k = k -1
        for j in range(0,i+1):
            print("*",end="")
        print("\r")
    n = n - 1
    for i in range(0,n):
        for j in range(0,n):
            print(end=" ")
        for j in range(0,i+1):
            print(end=" ")
        k = n
        for j in range(0,k-i):
            print("*",end="")
        print("\r")

pattern(10)