"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

先找到树1中和树2相同根节点的结点
然后再去判断左数和右树是否相同

判断树空时，应该先判断树2是否为空
    如果先判断树1是否为空，此时返回的是False
    但是如果此时树2也遍历完，应该返回的True
    就会导致结果错误
"""


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1AndTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def DoesTree1AndTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1AndTree2(pRoot1.left, pRoot2.left) and self.DoesTree1AndTree2(pRoot1.right, pRoot2.right)