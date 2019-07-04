#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
import math


def sum_of_squares(a,b):
    result = 0
    for i in range(a,b+1):
        result += math.pow(i,2)
    return result


def square_of_sums(a,b):
    result = 0
    for i in range(a,b+1):
        result += i
    return math.pow(result,2)

print(abs(sum_of_squares(1,100)-square_of_sums(1,100)))
