from collections import defaultdict
  
d = defaultdict(list)
for i in range(5):
    d[i].append(i)
      
print("Dictionary with values as list:")
print(d)
print(d.values())
print(d.keys())


# Default dicts are better bcoz it doesnt raise key value error


## Use case :

# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1

# sorted(d.items())
# [('i', 4), ('m', 1), ('p', 2), ('s', 4)]