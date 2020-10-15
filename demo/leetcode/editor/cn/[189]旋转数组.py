# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  说明: 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  要求使用空间复杂度为 O(1) 的 原地 算法。 
#  
#  Related Topics 数组 
#  👍 684 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rotate(nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方式一: 将最后一个元素弹出并插入到
        # for index in range(k):
        #     nums.insert(0, nums.pop())

        # 方法二: 三次反转
        size = len(nums)
        k = k % size
        def swap(arr, a, b):
            while a < b:
                temp = arr[a]
                arr[a] = arr[b]
                arr[b] = temp
                a, b = a + 1, b - 1
        swap(nums, 0, size - 1)
        swap(nums, 0, k - 1)
        swap(nums, k, size - 1)




        return nums

    print(rotate([1], 3))
# leetcode submit region end(Prohibit modification and deletion)
