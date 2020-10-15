# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 
# 的 min(ai, bi) 总和最大。 
# 
#  示例 1: 
# 
#  
# 输入: [1,4,3,2]
# 
# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
#  
# 
#  提示: 
# 
#  
#  n 是正整数,范围在 [1, 10000]. 
#  数组中的元素范围在 [-10000, 10000]. 
#  
#  Related Topics 数组 
#  👍 178 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def arrayPairSum(nums: List[int]) -> int:
        arr = [0] * 20001
        offset = 10000
        max_size = 0
        for ele in nums:
            arr[ele + offset] += 1

        flag = 1
        for i in range(-10000, 10001):

            if arr[i + offset] > 0:
                max_size += ((arr[i + offset] + flag) // 2) * i
                if (arr[i + offset]) % 2 != 0:
                    flag = 1 - flag
        return max_size

    print(arrayPairSum([1,4,3,2]))



        
# leetcode submit region end(Prohibit modification and deletion)
