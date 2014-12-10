#problem number 7

c=0
for num in range(1,200000):
    if all(num%i!=0 for i in range(2,num)) and c != 10002:
       print num,"#",c
       c += 1
