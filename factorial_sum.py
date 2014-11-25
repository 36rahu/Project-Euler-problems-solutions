"""
Question:

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
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
