"""
Question:6


The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_of_squre():
    sum = 0
    for i in range(0,101):
        sum += i*i
    return sum

def squre_of_sum():
    sum = 0
    for i in range(0,101):
        sum = sum + i
    sum =sum ** 2
    return sum

def sum_squre_diffrence():
    a = sum_of_squre()
    b = squre_of_sum()
    diff = b - a
    print "sum squre difrence",diff

if __name__ == '__main__':
    sum_squre_diffrence()
