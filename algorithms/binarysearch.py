def binarySearch(arr , ele):

    n = len(arr)
    beg_index = 0
    end_index = n - 1 

    while(beg_index <= end_index):
        midpoint_index = beg_index + (end_index - beg_index) // 2 
        midpoint = arr[midpoint_index]
        
        if(midpoint == ele):
            return midpoint

        elif (ele > midpoint):
            beg_index = midpoint + 1

        else :
            end_index = midpoint - 1 

    return None

array = [1 , 2 , 3 , 5 , 7 , 8 , 9]
element = 4

print(binarySearch(array , element))