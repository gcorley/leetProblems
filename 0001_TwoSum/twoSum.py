def two_sum(nums: list[int], target: int) -> list[int]:
    final = {}
    for i, num in enumerate(nums):
        num2 = target - num
        if num2 in final:
            return [final[num2], i]
        else:
            final[num] = i

    # final = []
    # for i, num in enumerate(nums):
    #     for ii, num2 in enumerate(nums):
    #         if i != ii:
    #             if num + num2 == target:
    #                 final.append(i)
    #                 final.append(ii)
    #                 return final
    # return final
