#problem number 30

def sumazation(num):
    string = str(num)
    re = 0
    for i in range(len(string)):
        po = int(string[i])**5
        re += po
    return re


x,main_result = 1000,0
while x != 1000000:
    result = sumazation(x)
    if result == x:
        main_result += result
        print "Itreations #",result
    x += 1

print "sum of all the numbers that can be written as the sum of fifth powers of their digits = ",main_result
