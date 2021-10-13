def solve(s,i,j,is_true):
    
    if i > j:
        return 0
        
    if i == j:
        
        if is_true:
            
            if s[i] == 'T':
                
                return 1
            else:
                
                return 0
        else:
            
            if s[i] == 'F':
                
                return 1
            else:
                
                return 0
                
    temp = 0
                
    for k in range(i+1,j,2):
        
        left_true = solve(s,i,k-1,True)
        left_false = solve(s,i,k-1,False)
        
        right_true = solve(s,k+1,j,True)
        right_false = solve(s,k+1,j,False)
        
        if s[k] == '&':
            
            if is_true:
                
                temp += left_true * right_true
                
            else:
                
                temp += left_true * right_false + left_false * right_true + left_false * right_false
                
        elif s[k] == '|':
            
            if is_true:
                
                temp += left_true * right_false + left_false * right_true + left_true * right_true
                
            else:
                
                temp +=  left_false * right_false
        
        elif s[k] == '^':
            
            if is_true:
                
                temp += left_true * right_false + left_false * right_true
                
            else:
                
                temp +=   left_true * right_true + left_false * right_false
        
    return temp

s = 'T^F|F'
print(solve(s,0,len(s)-1,True))
