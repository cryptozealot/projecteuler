#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

result = 0
i = 1
last = 0

while i < 4000000:
    if i % 2 ==0:
        sum += i
    i = i + last
    last = i - last

print(result)
