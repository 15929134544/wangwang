"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取
数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""

import heapq


class Solution:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        self.isfirst = True

    def Insert(self, num):
        # write code here
        if not self.min_heap:
            self.min_heap.append(num)
            self.max_heap.append(-num)
        elif self.isfirst and len(self.min_heap) == 1 and len(self.max_heap) == 1:
            self.isfirst = False
            if num > self.min_heap[0]:
                self.min_heap[0] = num
            else:
                self.max_heap[0] = -num
        else:
            if num >= -1 * self.max_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, -num)
        if len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -1 * heapq.heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -1 * heapq.heappop(self.max_heap))

    def GetMedian(self, n=None):
        # write code here
        if len(self.min_heap) == len(self.max_heap):
            return 0.5 * (-1 * self.max_heap[0] + self.min_heap[0])
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -1 * self.max_heap[0]