course = "Python for beginners" 

#String Methods

print(course.upper()) #Uppercase all
print(course.lower())   #Lowercase all
print(course.swapcase()) #SwapCase
print(course.capitalize()) #Capitalize first Word
print(course.title()) #Capitalize first letter of every word
print(course.replace('e' , 'f')) #Replace

print(course.find('n')) #Finds the appearance in ascending order
print(course.rfind('n'))  #Finds the appearance in descending order
print(course.index('n')) #Finds the appearance in ascending order
print(course.rindex('n'))  #Finds the appearance in descending order

#Difference between find and index
print(course.find('cat')) #Returns -1
# print(course.index('cat')) #Gives error

print(course.count('H'))  #counts the occurence
print(course.rstrip('7')) #Removes blank spaces

#Special Operators
print('Python' in course) #in operator
print('python' in course) #in operator -- returns a boolean value
#Python is case Sensitive
print(course[1:4]) #Slicing
print(course[ : : -1]) #Reverse a string

#Split
print(course.split(' '))

