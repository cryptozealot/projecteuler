#Find the sum of all the primes below two million.

result = 0
for possiblePrime in range(2, 2000001):

    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
       result += possiblePrime

print(result)
