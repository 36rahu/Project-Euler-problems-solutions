#probelm number 8

str1 = """long string ********1000 digits********"""
lis = []
c,i,j = 0,0,13
while j != 1001: 
    sum = 1
    for num in range(i,j):
        c += 1
        sum *= int(str1[num])
    j += 1
    i += 1
    lis.append(sum)
lis.sort()
print "Largest sum=", lis[-1]
