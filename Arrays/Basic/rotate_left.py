def rotateList(arr,d,n):
    arr[:]= arr[d:n] + arr[0:d]
    return arr

arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Rotated list is")
print(rotateList(arr,2,len(arr))) 