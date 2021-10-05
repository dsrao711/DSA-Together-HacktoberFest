
def quicksort(sequence) :
    length = len(sequence)
    
    if (length <= 1):
        return sequence
    else : 
        pivot = sequence.pop()

    lower_sequence = []
    upper_sequence = []
    
    for item in sequence :
        if(item < pivot):
            lower_sequence.append(item)
        else: 
            upper_sequence.append(item)
    return quicksort(lower_sequence) + [pivot] + quicksort(upper_sequence) 

print(quicksort([1 , 5 , 6, 3 , 5 , 3 , 0]))


