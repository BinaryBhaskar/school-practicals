def isprime(n):
    if n <=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


print(13, isprime(13))
print(16, isprime(16))