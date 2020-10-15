# 给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。 
# 
#  子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。 
# 
#  输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。 
# 
#  
# 
#  示例： 
# 
#  输入: "aba", "cdc", "eae"
# 输出: 3
#  
# 
#  
# 
#  提示： 
# 
#  
#  所有给定的字符串长度不会超过 10 。 
#  给定字符串列表的长度将在 [2, 50 ] 之间。 
#  
# 
#  
#  Related Topics 字符串 
#  👍 42 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
from typing import List


class Solution:
    def findLUSlength(strs: List[str]) -> int:
        size, arr1, arr2, res = -1, [], [""], []
        map1 = Counter(strs)
        for ele in map1:
            if map1[ele] == 1:
                arr1.append(ele)
            else:
                arr2.append(ele)
        for e1 in arr1:
            for e2 in arr2:
                if e1 not in e2:
                    res.append(e1)
        for ele in res:
            if size < len(ele):
                size = len(ele)
        return size

    print(findLUSlength(["aba","cdc","eae"]))
        
# leetcode submit region end(Prohibit modification and deletion)
