# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution(object):
    def twoSum(nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for key, value in enumerate(nums):
            hashmap[key] = value
        # for i, v in enumerate(nums):
        #     temp = target - v
        #     j = hashmap.get(temp)
        #     if j is not None and i != j:
        #         return [i, j]
        return hashmap

    print(twoSum([3, 2, 2, 4], 4))
# leetcode submit region end(Prohibit modification and deletion)
