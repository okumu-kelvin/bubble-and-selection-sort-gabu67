def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

input_list = [4, 5, 3, 4]
sorted_list = bubble_sort(input_list)
print("Output:", sorted_list)