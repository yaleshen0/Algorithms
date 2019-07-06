# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxDepth = 0
        if root == None:
            return maxDepth+1
        leftDepth = self.childDepth(root.left, maxDepth+1)
        rightDepth = self.childDepth(root.right, maxDepth+1)
        return max(leftDepth, rightDepth)
    def childDepth(self, root, maxDepth):
        leftDepth = rightDepth = maxDepth
        if root == None:
            return maxDepth+1
        if root.left != None:
            leftDepth = self.childDepth(root.left, maxDepth+1)
        if root.right != None:
            rightDepth = self.childDepth(root.right, maxDepth+1)
        return max(max(leftDepth, rightDepth), maxDepth)
        
rootNode = TreeNode(3)
rootNode.left = TreeNode(9)
rootNode.right = TreeNode(20)
rootNode.right.left = TreeNode(15)
rootNode.right.right = TreeNode(7)
# rootNode.right.left.left = TreeNode(2)
if __name__ == "__main__":
    # maxDepth = 1
    maxDepth = Solution().maxDepth(rootNode)
    print(maxDepth)