# 给定一个二进制数组， 计算其中最大连续1的个数。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
#  
# 
#  注意： 
# 
#  
#  输入的数组只包含 0 和1。 
#  输入数组的长度是正整数，且不超过 10,000。 
#  
#  Related Topics 数组 
#  👍 111 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMaxConsecutiveOnes(nums: List[int]) -> int:
        count = 0
        max_size = 0
        for ele in nums:
            if ele == 1:
                count += 1
            else:
                if max_size < count:
                    max_size = count
                count = 0
        if max_size < count:
            max_size = count
        return max_size



    print(findMaxConsecutiveOnes([1,1,1,0,1,1]))

# leetcode submit region end(Prohibit modification and deletion)
