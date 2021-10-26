# Rearrange all elements of array which are multiples of 10 in the end of the array

multiples = []
def sortMultiples(arr, n):
    if(n == 0):
        return -1
    for i in arr:
        if(i % 10 == 0):
            multiples.append(i)
            arr.remove(i)            
    return arr+multiples

if __name__ == '__main__':
    
    lst = []
    n = int(input("Enter number of elements : "))
    
    for i in range(0, n):
        ele = int(input())
        lst.append(ele) 
     
    array = sortMultiples(lst, n)
    for i in array:
        print(i, end = " ")
 
