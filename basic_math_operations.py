def basic_op(operator, value1, value2):
    if operator == '+':
        eqn = value1 + value2
    elif operator == '-':
        eqn = value1 - value2
    elif operator == '*':
        eqn = value1 * value2
    elif operator == '/':
        eqn = value1 / value2
    return eqn

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

print(basic_op('*', 2, 5))
print(basic_op('/', 49, 7))
print(basic_op('-', 15, 20))