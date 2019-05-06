def remove_smallest(numbers):
    mynumbers = numbers.copy()
    if len(mynumbers) <= 1:
        return []
    else:
        mynumbers.remove(min(mynumbers))
    return mynumbers

print(remove_smallest([3, 4, 2, 2, 6]))
