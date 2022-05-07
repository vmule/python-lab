def numof3(n):
    total = 0
    while (n > 10):
        if (n % 10) == 3: total += 1
        n /= 10
    if n == 3: total += 1
    return total

def count3(n):
    total = 0
    for x in range(1, n+1):
        total += numof3(x)
    return total


a = count3(333)
print(a)
