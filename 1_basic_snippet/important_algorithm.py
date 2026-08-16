# Kadane's Algorithm: O(n) -- find min/max sum in array
def kadanes(nums):
    max_sum = nums[0]
    curr_sum = 0

    for n in nums:
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        max_sum = max(max_sum, curr_sum)

    return max_sum


# Kadane's Algorithm: O(n) -- find min/max sum in array
def kadanes_with_index(nums):
    max_sum = nums[0]
    curr_sum = 0

    max_i = max_j = 0
    i = j = 0

    while j < len(nums):
        if curr_sum < 0:
            i = j
            curr_sum = 0

        curr_sum += nums[j]
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_i, max_j = i, j

        j += 1

    return nums[max_i : max_j + 1]


print(kadanes_with_index([4, -1, 2, -7, 3, 4]))
