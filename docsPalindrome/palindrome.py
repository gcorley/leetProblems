def is_palindrome(x: int) -> bool:
    list1 = [num for num in str(x)]
    list2 = list1.copy()
    list2.reverse()
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
