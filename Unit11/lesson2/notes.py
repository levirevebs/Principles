def print_median_even(list, number):
    median_index2 = number // 2
    median_index1 = median_index2 - 1
    middle1 = list[median_index1]
    middle2 = list[median_index2]
    median = (middle1 + middle2) / 2
    print("The median of the list is", median)

def print_median_odd(list, number):
    median_index = number // 2
    print("The median of the list is:", list[median_index])

def print_median(list):
    list.sort()
    number = len(list)
    if number % 2 == 0:
        print_median_even(list, number)
    else:
        print_median_odd(list, number)

list_1 = [1, 2, 3, 4, 5]
print_median(list_1)
list_2 = [4, 31, 1, 2]
print_median(list_2)
