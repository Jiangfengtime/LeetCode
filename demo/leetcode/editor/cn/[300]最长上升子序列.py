# 给定一个无序的整数数组，找到其中最长上升子序列的长度。 
# 
#  示例: 
# 
#  输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。 
# 
#  说明: 
# 
#  
#  可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
#  你算法的时间复杂度应该为 O(n2) 。 
#  
# 
#  进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
#  Related Topics 二分查找 动态规划 
#  👍 967 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def lengthOfLIS(nums: List[int]) -> int:
        # res = 1
        # for index in range(1, len(nums)):
        #     if nums[index] > nums[index - 1]:
        #         res += 1
        # return res

        if not nums:
            return 0
        res = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    res[i] = max(res[i], res[j] + 1)
        return res[len(nums) - 1]

    print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
        
# leetcode submit region end(Prohibit modification and deletion)
