def bubble_sort(custom_list):
    for i in range(len(custom_list) - 1):
        for j in range(len(custom_list - i - 1)):
            if custom_list[j] > custom_list[j + 1]:
                custom_list[j], custom_list[j + 1] = custom_list[j + 1], custom_list[j]
    print(custom_list)


c_list = [3, 2, 4, 5, 6, 7, 1, 8, 9, 0]
# bubble_sort(c_list)
# print(c_list)


def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j + 1]:
                customList[j], customList[j + 1] = customList[j + 1], customList[j]
    print(customList)


def bubble_sort(custom_list):
    for i in range(len(custom_list) - 1):
        swapped = False
        for j in range(len(custom_list) - i - 1):
            if custom_list[j] > custom_list[j + 1]:
                custom_list[j], custom_list[j + 1] = custom_list[j + 1], custom_list[j]
                swapped = True
        if not swapped:
            break
    print(custom_list)


bubble_sort(c_list)
bubbleSort(c_list)
