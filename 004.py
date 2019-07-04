#Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False


result = 0
for i in range(999,900,-1):
    for j in range(999,900,-1):
        if is_palindrome(i*j) and i*j > result:
            result = i*j # product
            print(i) # first number
            print(j) # second number

print(result)
