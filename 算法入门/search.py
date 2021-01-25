# 线性查找
def linear_search(li, val):
    for index, v in enumerate(li):
        if v == val:
            return index
        else:
            return None


# 二分查找
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 说明候选区一直有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid的左侧
            right = mid - 1
        else:  # li[mid] > val  待查找的值在mid的右侧
            left = mid + 1
    else:
        return None
