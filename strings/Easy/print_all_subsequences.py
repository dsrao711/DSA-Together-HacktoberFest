
# Python Implementation of the approach
import itertools
 
def Sub_Sequences(STR):
    combs = []
    for l in range(1, len(STR)+1):
        combs.append(list(itertools.combinations(STR, l)))
    for c in combs:
        for t in c:
            print (''.join(t), end =' ')
 
# Testing with driver code
if __name__ == '__main__':
    Sub_Sequences('abc')