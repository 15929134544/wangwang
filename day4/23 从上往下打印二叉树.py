"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""


def PrintFromTopToBottom(self, root):
    if not root:
        return []
    currentStack = [root]
    res = []
    while currentStack:
        nextStack = []
        for i in currentStack:
            if i.left: nextStack.append(i.left)
            if i.right: nextStack.append(i.right)
            res.append(i.val)
        currentStack = nextStack
    return res