def armstrong(num):
    exponent = len(str(num))
    sum = 0
    for n in str(num):
        sum += int(n)**exponent
    return num == sum

print(1634,armstrong(1634))
print(123,armstrong(123))