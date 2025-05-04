def selection_sort(custom_list):
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i + 1, len(custom_list)):
            if custom_list[min_index] > custom_list[j]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)


c_list = [3, 2, 4, 5, 6, 7, 1, 8, 9, 0]

selection_sort(c_list)
