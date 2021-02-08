# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 在一个ListNode外面包了一层,帮我们比较两个ListNode，取最小的
class MyListNode:
    def __init__(self, l:ListNode):
        self.l = l
    # 等于的情况
    def __eq__(self, other):
        # 自己的值和另外一个ListNode的值相等
        return self.l.val == other.l.val
    # 小于的情况
    def __lt__(self, other):
        # 小于
        return self.l.val < other.l.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 重要
        # heap/priority Queue

        dummyhead = ListNode(0)
        curr = dummyhead

        # 把当前的所有ListNode包裹一下并且都放到heap中
        heap = [MyListNode(i) for i in lists if i]

        # heapify可以把list变成heap的形式
        heapq.heapify(heap)

        while heap:
            # 从heap里面拿取一个MyListNode, .l就是将他变成ListNode，便于操作
            i = heapq.heappop(heap).l
            curr.next = ListNode(i.val)
            curr = curr.next

            # 判断拿出来的结点后面是否还有元素
            if i.next:
                heapq.heappush(heap, MyListNode(i.next))
        return dummyhead.next