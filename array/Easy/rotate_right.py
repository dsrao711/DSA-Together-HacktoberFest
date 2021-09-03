def rotateList(arr,d,n):
    arr[:]=arr[n-d:n]+arr[0:n-d]
    return arr

# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Rotated list is")
print(rotateList(arr,2,len(arr))) 