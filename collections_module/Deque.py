# Implementing the various inbuilt methods provided by deque

from collections import deque

#Declare a Deque

queue = deque([1 , 2 , 9 , 9 , 9 , 9, 3 ])

print(deque)

#Operations 

# 1. append() : Inserts at right end of the dequeue
queue.append(4)
print(queue)

#2 . appendleft() : Inserts at the left end of the dequeue
queue.appendleft(2)
print(queue)

# 3. pop() : Deletes element from right end of dequeue
queue.pop()
print(queue)

# 4 . popleft() : Deletes element from left end of queue
queue.popleft()
print(queue)

#5 . index(ele , beg , end) : Returns first occurence of the ele from the range(beg,end)
queue.index(9 , 1 , 4)
print(queue)

# 6 .  insert( i , ele ): Inserts element 'ele' at ith position
queue.insert(2 , 8)
print(queue)

# 7 . remove(ele) : Removes first occurence of the element 'ele'
queue.remove(1)
print(queue)

# 8 . count(ele) : Returns the total number of occurences of the element 'ele' 
queue.count(2)
print(queue)

# 9. extend(iterable) : Adds list of elements in the arguement at the right end of dequeu
queue.extend([2,3,5,6])
print(queue)

#10 . extendleft(iterable) : Adds list of elements in the arguement at the left end of dequeu
queue.extendleft([2,3,5,6])
print(queue)

#11 . reverse() : Reverses the dequeue
queue.reverse()
print(queue)

#12. rotate(i) : Rotates the Dequeue
#If the arguement is positive - rotate the dequeue to right by i
#If the arguement is -ve - rotate the dequeue to left by i

queue.rotate(2)
print(queue)