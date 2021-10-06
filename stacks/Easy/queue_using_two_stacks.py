# Approach : 
# https://www.geeksforgeeks.org/queue-using-stacks/


#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    
    while(len(stack1) != 0):
        stack2.append(stack1.pop())
    stack1.append(x)
    while(len(stack2) != 0):
        stack1.append(stack2.pop())
        


#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    ele = -1
    if(len(stack1) != 0):
        ele = stack1.pop()
    
    return ele

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()
