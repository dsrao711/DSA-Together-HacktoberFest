def square_nums(nums):
    for i in nums : 
        yield (i*i)

my_nums = square_nums([1,2,3,4,5])

# Not recommended 
print(list(my_nums))



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
