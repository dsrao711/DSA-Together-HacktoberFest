# Python program to display all the prime numbers within an interval
imp
lower = 2
upper = 10

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, (num//2)+1):
           if (num % i) == 0:
               break
        else:
            print(num)
