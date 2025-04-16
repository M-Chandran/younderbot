def merge(arr1, arr2):
    merged = arr1 + arr2
    return sorted(merged)
array1 = [1, 3, 5]
array2 = [2, 4, 6]
merged_array = merge(array1, array2)
print("Merged array:", merged_array)
