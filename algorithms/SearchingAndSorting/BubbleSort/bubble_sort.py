arr=input("Enter array elements").split(' ')
arr=[int(x) for x in arr]

for i in range(len(arr)):
    for j in range(len(arr)-1-i):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]

print("Sorted array is:",arr)

"""
Problem Statement: Sort array using bubble sort technique

Sample Input/Output:
Input: 4 2 5 3 1
Output: 1,2,3,4,5

Time Complexity: O(n^2) (worst)
Space Complexity: O(1)
"""