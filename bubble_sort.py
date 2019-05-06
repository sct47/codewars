def bubble_sort(list):
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        for i in range(len(list) - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = temp
                is_sorted = False
        is_sorted = True
    return sorted_list

print(bubble_sort([3, 2, 1]))