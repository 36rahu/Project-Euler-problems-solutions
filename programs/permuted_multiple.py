
#problem number 52

x,st = 2,False
while(st != True):
    x2,x3,x4,x5,x6 = 2*x,3*x,4*x,5*x,6*x
    sort_2x = sorted(str(x2))
    sort_3x = sorted(str(x3))
    sort_4x = sorted(str(x4))
    sort_5x = sorted(str(x5))
    sort_6x = sorted(str(x6))
    if sort_2x == sort_3x and sort_2x == sort_4x and sort_2x == sort_5x and sort_2x == sort_6x:
        st = True
        print "Permutated multiple is ",x
    else:
        x += 1
        st = False
        print "Itreation ",x
