result = 0
i = 1
last = 0

while i < 4000000:
    if i % 2 ==0:
        sum += i
    i = i + last
    last = i - last

print(result)
