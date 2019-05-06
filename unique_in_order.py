# def unique_in_order(iterable):
#     unique = []
#     for x in iterable:
#         if len(unique) < 1 or not x == unique[len(unique) - 1]:
#             unique.append(x)
#     return unique

# unique_in_order('AAABCcD')

def unique_in_order(iterable):
    uniqueList = []
    for x in iterable:
        if len(uniqueList) == 0 or x != uniqueList[-1]:
            uniqueList.append(x)
    print(uniqueList)

unique_in_order('AABCCDDEEFF1')

def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result