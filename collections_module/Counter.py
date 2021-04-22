from collections import Counter 
  
print(Counter(['B','B','A','B','C','A','B',
               'B','A','C']))

print(Counter({'A':3, 'B':5, 'C':2}))
    
print(Counter(A=3, B=5, C=2))

c = Counter(a=4, b=2, c=0, d=-2)
print(sorted(c.elements()))
print(sum(c.values())  )

#Most common
print(Counter('abracadabra').most_common(3))