# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  示例: 
# 
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#  
# 
#  进阶: 
# 
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
#  Related Topics 数组 分治算法 动态规划 
#  👍 2402 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxSubArray(nums: List[int]) -> int:
        # 方法一:
        # max_size = nums[0]
        # arr = [0 for _ in range(len(nums))]
        # for i in range(1, len(nums)):
        #     arr[i] = max(arr[i - 1] + nums[i], nums[i])
        #     max_size = max(max_size, arr[i])
        #
        # return max_size


        max_size = nums[0]
        temp = 0
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            max_size = max(max_size, temp)
        return max_size

    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

# leetcode submit region end(Prohibit modification and deletion)
