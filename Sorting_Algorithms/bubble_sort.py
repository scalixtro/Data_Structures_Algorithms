def bubble_sort(nums):
    """
    Implementation of bubble sort algorithm.

    Keyword Arguments:
        - nums: List of numbers to sort.
    """
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

if __name__ == '__main__':
    my_list = [5, 10, 3 , 2, 100, -5, 0]
    print("Unsorted list: ", my_list)
    bubble_sort(my_list)
    print("Sorted List: ", my_list)