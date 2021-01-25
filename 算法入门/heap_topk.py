# 堆排序
# 比较排序
def sift(li, low, high):
    """

    :param li:列表
    :param low:堆的堆顶位置（根节点位置）
    :param high:堆的最后一个元素的位置
    :return:
    """
    i = low
    j = 2*i+1   # j是左孩子
    tmp = li[low]   # 把堆顶存起来
    while j<= high: # 只要j位置有数
        if j+1<= high and li[j+1] < li[j]:
            j += 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j   # 往下找一层
            j = 2*i+1
        else:  # tmp更大,把tmp放到i的位置
            # li[i] = tmp # 把tmp放到某一级领导的位置
            break
    # else:
    #     li[i] = tmp
    li[i] = tmp


def topk(li, k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    # 1.建堆
    for i in range(k, len(li)-1):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)
    # 2.遍历
    for i in range(k-1, -1,-1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap
    # 出数
    return heap


# 测试
import random
li = list(range(1000))
random.shuffle(li)

print(topk(li, 10))



