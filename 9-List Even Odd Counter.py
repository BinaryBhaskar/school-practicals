def counter(list):
    counteven = countodd = 0
    for i in list:
        if i%2 == 0:
            counteven += 1
        else:
            countodd += 1
    print(f"Even Numbers:{counteven}\nOdd Numbers:{countodd}")


list = [13,74,34,70,38,85,57]
counter(list)