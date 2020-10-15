# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


def commonPrefix(leftLCP, rightLCP):
    if not leftLCP or not rightLCP:
        return ""
    length = min(len(leftLCP), len(rightLCP))
    for i in range(length):
        if leftLCP[i] != rightLCP[i]:
            if i == 0:
                return ""
            return leftLCP[:i]
    if len(leftLCP) > len(rightLCP):
        return rightLCP
    else:
        return leftLCP


def LCP(strs, left, right):
    if left == right:
        return strs[left]
    else:
        mid = (left + right) // 2
        leftLCP = LCP(strs, 0, mid)
        rightLCP = LCP(strs, mid + 1, right)
        return commonPrefix(leftLCP, rightLCP)


def longestCommonPrefix(strs: List[str]):
    if not strs:
        return ""
    return LCP(strs, 0, len(strs) - 1)


print(longestCommonPrefix(["323", "342", "3211", "324"]))
# leetcode submit region end(Prohibit modification and deletion)

# ["flower","flow","flight"]
