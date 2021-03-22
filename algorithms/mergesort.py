def mergesort(arr):

    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[: mid]
    right = arr[mid:]

    mergesort(left)
    mergesort(right)

    merge_sorted_list(left, right, arr)


def merge_sorted_list(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    while (i < len_a and j < len_b):
        
        if(a[i] <= b[j]):
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1

        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[j] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':

    test_cases = [
        [0, 1, 5, 3, 2, 7],
        [1, 3, 4, 2, 55, 2, 99, 33],
        [1, 2],
        []
    ]

    for arr in test_cases:
        mergesort(arr)
        print(arr)
