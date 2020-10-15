# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#  
# 
#  示例 2： 
# 
#  输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  -10000 <= A[i] <= 10000 
#  A 已按非递减顺序排序。 
#  
#  Related Topics 数组 双指针 
#  👍 106 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        result = []
        while left <= right:
            if A[left] * A[left] <= A[right] * A[right]:
                result.append(A[right] * A[right])
                right -= 1
            else:
                result.append(A[left] * A[left])
                left += 1
        result.reverse()
        return result
    print(sortedSquares([-7,-3,2,0,0,0,3,11]))
        
# leetcode submit region end(Prohibit modification and deletion)
