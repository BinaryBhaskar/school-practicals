def fibonacci(n):
    n1, n2 = 0, 1
    next = n2  
    count = 1
    while count <= n:
        print(next, end=" ")
        count += 1
        n1, n2 = n2, next
        next = n1 + n2
    print()

fibonacci(7)