def factorial_sum():
    j,su = 0,1
    for i in range(1,101):
        su *= i
    st = str(su)
    le = len(st)
    while(le != 0):
        j += int(st[le-1])
        le -= 1
    return j
    
if __name__ == '__main__':
    digit_sum = factorial_sum()
    print "Sum of Factorial umber 100! =",digit_sum

