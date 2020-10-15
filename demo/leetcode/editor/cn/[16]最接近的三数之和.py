# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSumClosest(nums: List[int], target: int) -> int:
        nums.sort()
        ans_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(ans_sum - target) > abs(curr_sum - target):
                    ans_sum = curr_sum
                if curr_sum > target:
                    right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    return target
        return ans_sum




        return sum1

    print(threeSumClosest([1, 6, 7, 2, 4], 5))
# leetcode submit region end(Prohibit modification and deletion)
