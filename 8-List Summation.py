def list_sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum


list = [13,74,34,70,38,85,57]
print("Sum of list:" , list_sum(list))