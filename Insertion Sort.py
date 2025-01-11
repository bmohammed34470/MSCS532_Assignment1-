def insertion_sort_decreasing(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Move elements of arr[0..i-1] that are smaller than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Taking array input from the user
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

sorted_arr = insertion_sort_decreasing(arr)
print("Sorted array in monotonically decreasing order:", sorted_arr)
