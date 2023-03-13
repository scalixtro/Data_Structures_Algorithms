def merge(list1, list2):
    """
    Combine and sort two given lists of numbers.

    Keyword Arguments:
        - list1: List of numbers.
        - list2: List of numbers.
    """
    p1 = 0
    p2 = 0
    merged_list = []
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] < list2[p2]:
            merged_list.append(list1[p1])
            p1 += 1
        else:
            merged_list.append(list2[p2])
            p2 += 1
    # If there are items remaining in list1
    while p1 < len(list1):
        merged_list.append(list1[p1])
        p1 += 1
    # If there are items remaining in list2
    while p2 < len(list2):
        merged_list.append(list2[p2])
        p2 += 1
    return merged_list


def merge_sort(nums):
    """
    Implementation of Merge Sort algorithm.

    Keyword Arguments:
        - nums: List of numbers to sort.
    """
    if len(nums) == 1:
        return nums
    mid_index = len(nums) // 2
    return merge(merge_sort(nums[:mid_index]),
                 merge_sort(nums[mid_index:])
                 )

if __name__ == '__main__':
    my_list = [0, -50, 1.2, 4, 10, 3, 3, 1]
    print("Unsorted list: ", my_list)
    # Expected output: [-50, 0, 1, 1.2, 3, 3, 4, 10]
    print("Sorted list: ", merge_sort(my_list))
    
