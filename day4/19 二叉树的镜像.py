"""
操作给定的二叉树，将其变换为源二叉树的镜像。

注：交换根节点下面的两个孩子，相当于交换两个孩子
连带下面的子树。
"""


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return root
        node = root.left
        root.left = root.right
        root.right = node
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root