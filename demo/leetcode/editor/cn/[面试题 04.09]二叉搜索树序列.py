# 从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉搜索树，输出所有可能生成此树的数组。 
# 
#  
# 
#  示例： 
# 给定如下二叉树 
# 
#          2
#        / \
#       1   3
#  
# 
#  返回： 
# 
#  [
#    [2,1,3],
#    [2,3,1]
# ]
#  
#  Related Topics 树 动态规划 
#  👍 40 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
# leetcode submit region end(Prohibit modification and deletion)
