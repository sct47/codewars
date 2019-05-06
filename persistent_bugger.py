from functools import reduce
import operator

def persistence(num):
    if len(str(num)) == 1:
        return 0
    val = reduce(operator.mul, map(int, str(num)))
    return 1 + persistence(val)

print(persistence(39))
# 3
print(persistence(25))
# 2

