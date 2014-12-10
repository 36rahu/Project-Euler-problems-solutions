#problem number 25

"""2 terms extra taken for the declaration"""
stack,n,su,k = [1,1],0,0,0
while(n != 10000000):
    su = int(stack[k]) + int(stack[k+1])
    stack.append(su)
    n += 1
    k += 1
    if len(str(su)) == 1000:
        print "1000 term fibinacci number having in",n+2,"term"
        break

    
    
