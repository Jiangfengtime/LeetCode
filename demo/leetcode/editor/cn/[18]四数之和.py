# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 
# 
#  注意： 
# 
#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        size = len(nums)
        res = []
        for k1 in range(size - 3):
            for k2 in range(k1 + 1, size - 2):
                left = k2 + 1
                right = size - 1
                while left < right:
                    ele = [nums[k1], nums[k2], nums[left], nums[right]]
                    if sum(ele) == target and ele not in res:
                        res.append(ele)
                        left += 1

                    elif sum(ele) < target:
                        left += 1
                    else:
                        right -= 1
        return res
    print(fourSum([1,-2,-5,-4,-3,3,3,5], -11))


# leetcode submit region end(Prohibit modification and deletion)
