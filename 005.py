#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def devisible_by_1_to_20(n):
    primes = [7,9,11,13,16,17,19]
    for i in primes:
        if n % i != 0:
            return False
    return True

number = 2000
while True:
    if devisible_by_1_to_20(number):
        print(number)
        break
    number +=160 #reduce for accuracy
