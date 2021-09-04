import sys

list_a = [8,7,8,8,8]

max_a = list_a[0]

for i in range(1 , len(list_a)):
    if(list_a[i] > max_a):
        max_a = list_a[i]

# print(max_a)
        
max_b = -sys.maxsize - 1

for i in range(1 , len(list_a)):

    if(list_a[i] < max_a and list_a[i] > max_b):
        max_b = list_a[i]
        
print(max_b)