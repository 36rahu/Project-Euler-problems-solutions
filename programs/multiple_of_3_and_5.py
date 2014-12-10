#problem number 1 and 2

def multiple():
    total = 0
    for i in range(0,1000):
        if i % 3 == 0 or i % 5 == 0:
            total = total + i
    return total


def fibi_add():
    total = 2
    tplus = 1
    teven = 0
    while total < 4000000:
        if total % 2 == 0:
            teven = total + teven
        total = total + tplus
        tplus = total - tplus 
    return teven

if __name__ == '__main__':
	multi = multiple()
	print "Multiple of 3 and 5 = ",multi
	fibi = fibi_add()
	print "Even fibinacci numbers sum = ",fibi
