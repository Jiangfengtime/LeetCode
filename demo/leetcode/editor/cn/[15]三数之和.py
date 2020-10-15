# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def threeSum(nums: List[int]):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # result = []
        # nums.sort()
        # size = len(nums)
        # for index in range(1, size - 1):
        #     left = index - 1
        #     right = index + 1
        #     if index < size - 1 and nums[index] == nums[index + 1]:
        #         continue
        #     while left >= 0 and right < size:
        #
        #         if nums[left] + nums[index] + nums[right] == 0:
        #             temp = [nums[left], nums[index], nums[right]]
        #             if temp not in result:
        #                 result.append(temp)
        #             left -= 1
        #             right += 1
        #         elif nums[left] + nums[index] + nums[right] > 0:
        #             left -= 1
        #         else:
        #             right += 1
        # result.sort()
        # return result

        size = len(nums)
        result = []
        if not nums or size < 3:
            return []
        nums.sort()
        for i in range(size):
            if nums[i] > 0:
                return result
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = size - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return result






    print(threeSum([-1, 0, 1, 2, -1, -4]))
# leetcode submit region end(Prohibit modification and deletion)
