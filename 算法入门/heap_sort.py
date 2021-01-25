# 堆排序
def sift(li, low, high):
    """

    :param li:列表
    :param low:堆的堆顶位置（根节点位置）
    :param high:堆的最后一个元素的位置
    :return:
    """
    i = low     # i是指向根节点
    j = 2*i+1   # j是左孩子
    tmp = li[low]   # 把堆顶存起来
    while j<= high: # 只要j位置有数
        if j+1<= high and li[j+1] > li[j]:  # 首先保证右孩子有，并且比较大
            j += 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j   # 往下找一层
            j = 2*i+1
        else:  # tmp更大,把tmp放到i的位置
            # li[i] = tmp # 把tmp放到某一级领导的位置
            break
    # else:
    #     li[i] = tmp
    li[i] = tmp


def heap_sort(li):
    n = len(li)
    for i  in range(n-2 // 2, -1, -1):    # 从孩子找父亲
        # i代表了建堆的时候，调整的部分的下标
        sift(li, i, n-1)
    # 建堆就完成了
    # 挨个输出
    for i in range(n-1, -1, -1):
        # i 指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)    # i-1是新的high


li = [i for i in range(100)]
import random
random.shuffle(li)
print(li)

heap_sort(li)
print(li)