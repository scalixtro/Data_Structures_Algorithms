def insertion_sort(nums: list[int]):
    for i in range(1, len(nums)):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums

if __name__ == '__main__':
    print(insertion_sort([4, 2, 6, 5, 1, 3]))