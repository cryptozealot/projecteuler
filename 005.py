#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def devisible_by_1_to_20(n):
    for i in range(3,21):
        if n % i != 0:
            return False
    return True

number = 20
while True:
    if devisible_by_1_to_20(number):
        print(number)
        break
    number +=20
