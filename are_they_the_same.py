def comp(array1, array2):
    return sorted([i ** 2 for i in array1]) == sorted(array2)

print(comp([2, 3, 3], [4, 9, 9]))