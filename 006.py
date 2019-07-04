#What is the 10 001st prime number?

primes = []
for possiblePrime in range(2, 1000000):


    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1):
        if possiblePrime % num == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(possiblePrime)

print(primes[10000])
