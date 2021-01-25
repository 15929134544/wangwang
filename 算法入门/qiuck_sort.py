def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边空位上
        print(li)
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上
        print(li)
    li[left] = tmp  # 把tmp归位
    return left


def quick_sort(li, left, right):
    if left < right:    # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
# print(li)
# partition(li, 0, len(li)-1)
# print(li)
quick_sort(li, 0, len(li)-1)
print(li)