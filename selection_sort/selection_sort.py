def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]<arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

input_list = [29, 10, 14, 37, 14]
sorted_list = selection_sort(input_list)
print("Expected output:", sorted_list)