def sum_two_smallest_numbers(numbers):
    #your code here
    numbers.sort(key=int)
    return (numbers[0] + numbers[1])


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


    