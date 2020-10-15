# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。 
# 
#  你可以返回满足此条件的任何数组作为答案。 
# 
#  
# 
#  示例： 
# 
#  输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 5000 
#  0 <= A[i] <= 5000 
#  
#  Related Topics 数组 
#  👍 153 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortArrayByParity(A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        while True:
            if left < right:
                while A[left] % 2 == 0 and left < right:
                    left += 1
                while A[right] % 2 == 1 and left < right:
                    right -= 1
                A[left], A[right] = A[right], A[left]

            else:
                break

        return A

    print(sortArrayByParity([0]))

# leetcode submit region end(Prohibit modification and deletion)
