def max_crossing_subarray(arr, low, mid, high):

    left_sum = -1
    current_sum = 0                      # start, stop, step - downto low
    for i in range(mid, low-1, -1):      # mid,   low-1, i--
        current_sum = current_sum + arr[i]
        left_sum = max(left_sum, current_sum)

    right_sum = -1
    current_sum = 0                      # start, stop ,step - to high
    for i in range(mid+1, high, 1):      # mid+1, high, i++
        current_sum = current_sum + arr[i]
        right_sum = max(right_sum, current_sum)

    return left_sum + right_sum


def max_subarray(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    return max(
        max_subarray(arr, low, mid),
        max_subarray(arr, mid+1, high),
        max_crossing_subarray(arr, low, mid, high)
    )

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(arr, 0, len(arr) - 1)
print("Maximum subarray sum:", result)