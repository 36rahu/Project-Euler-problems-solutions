#problem number 4

lis = []
k = 1
for i in range(900,1000):
    for j in range(900,1000):
        k = i * j
        lis.append(k)
lis.sort()
l = len(lis)
while(l != 0):
    str1 = str(lis[l - 1])
    if str1 == str1[::-1]:
        print "largest palindrome made from the product of two 3-digit numbers = ",str1
        break
    else:
        l -= 1
