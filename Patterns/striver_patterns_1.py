# https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

n = int(input("Enter number of rows "))
print("---- Pattern1 ----")
for i in range(1 , n+1):
    print("*"*n)

print("---- Pattern2 ----")
for i in range(1 , n+1):
    print("*"*i)

print("---- Pattern3 ----")
for i in range(1 , n+1):
    for j in range(1 , i+1):
        print(j , end="")
    print()

print("---- Pattern4 ----")
for i in range(1 , n+1):
    print(str(i)*i)

print("---- Pattern5 ----")
for i in range(n , 0 , -1):
    print("*"*i)

print("---- Pattern6 ----")
for i in range(n+1 , -1 , -1):
    for j in range(1 ,i):
        print(j , end="")
    print()






