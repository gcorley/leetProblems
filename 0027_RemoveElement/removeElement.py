def remove_element(nums: list[int], val: int) -> list[int]:
    # x = 0
    # for num in nums:
    #     if num != val:
    #         nums[x] = num
    #         x += 1

    x = nums.count(val)
    for count in range(x):
        curr_index = nums.index(val)
        nums[curr_index] = nums[-1]
        nums = nums[:-1]

    return nums
