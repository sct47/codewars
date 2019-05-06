def findSum(number):
    multiples = []
    for i in range(number+1):
        if i % 3 == 0:
            multiples.append(i)
        elif i % 5 == 0:
            multiples.append(i)
    return sum(multiples)

print(findSum(10))


    
