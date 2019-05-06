def positive_sum(arr):
    posnumbers = []
    for x in arr:
        if x > 0:
            posnumbers.append(x)
    return sum(posnumbers)

print(positive_sum([]))

