word = "bat"

op = word[0] + word[-1]
nums = [1,1,1,2,3,3]

from collections import Counter
d = Counter(nums)

print(len(list([item for item in d if d[item]>1]))) 

    
