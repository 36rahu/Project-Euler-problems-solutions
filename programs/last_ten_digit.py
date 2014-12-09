#problem no 48
su = 0
for i in range(1,1001):
    i = i ** i
    su += i
str1 = str(su)
print "last ten digit",str1[-10:]    
