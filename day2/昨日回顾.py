"""
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


# def find(self, ArrayList, target):
#     rows = len(ArrayList[0]) - 1
#     cols = len(ArrayList) -1
#     i = 0
#     j = cols
#     while j >= 0 and i <= rows:
#         if ArrayList[i][j] == target:
#             return True
#         elif ArrayList[i][j] < target:
#             i += 1
#         else:
#             j -= 1
#     return False

"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""


# def change(s):
#     return '%20'.join(s.splite(' '))

"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""
# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#     def tail_to_head(self, ListNode):
#         list1 = []
#         while ListNode:
#             list1.append(ListNode.val)
#             ListNode = ListNode.next
#         return list1[::-1]


"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。
"""

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# class Solution:
#     def pre_tin_tree(self, pre, tin):
#         if not pre or not tin:
#             return None
#         root = TreeNode(pre.pop(0))
#         index = tin.index(root.val)
#         root.left = self.pre_tin_tree(pre, tin[:index])
#         root.right = self.pre_tin_tree(pre, tin[index+1:])
#         return root

"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""


# class Solution:
#     def __init__(self):
#         self.stack1 = []
#         self.stack2 = []
#
#     def push(self, node):
#         self.stack1.append(node)
#
#     def pop(self):
#         if not self.stack2:
#             while self.stack1:
#                 self.stack2.append(self.stack1.pop())
#
#         if self.stack2:
#             return self.stack2.pop()
#
#         return -1

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0
"""


# class Solution:
#     def minNumberInRotateArray(self, rorateArray):
#         high = 0
#         low = len(rorateArray) - 1
#         while low <= high:
#             mid = (low+high) // 2
#             if rorateArray[mid] > rorateArray[high]:
#                 low = mid + 1
#             else:
#                 high = mid
#         return rorateArray[low]
#
#