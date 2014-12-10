#problem number 16

i,j = 0,2 ** 1000
st = str(j)
le = len(st)
while le != 0:
    i += int(st[le-1])
    le -= 1
print "sum of the digits of the number 2**1000 = ",i
