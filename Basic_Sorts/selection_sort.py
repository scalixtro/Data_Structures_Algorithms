def selection_sort(nums):
    """
    Selection Sort implementations

    Keyword Arguments:
        - nums: List of numbers to sort.
    """
    for i in range(len(nums) - 1):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


if __name__ == '__main__':
    print(selection_sort([0, 10, 12, 13, -1]))