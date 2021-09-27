string = "Test String"
key = "4381"

k_o =  key[0] + key[1]
k_e =  key[2] + key[3]
final_op = ""

for i in range(0 , len(string)):
    if(i % 2 == 0):
        op = ord(string[i])
        print(op)
        xor = hex((int(op)) ^ (int(k_o)) )
        final_op.join(str(op))
        
    else:
        op = ord(string[i])
        xor = hex((int(op)) ^ (int(k_e)) )
        final_op.join(str(xor))
        
        
print(final_op)