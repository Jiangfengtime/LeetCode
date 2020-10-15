# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。 
# 
#  示例 : 
# 
#  输入: [1,2,1,3,2,5]
# 输出: [3,5] 
# 
#  注意： 
# 
#  
#  结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。 
#  你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？ 
#  
#  Related Topics 位运算 
#  👍 270 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNumber(nums: List[int]) -> List[int]:
        res, first, second = 0, 0, 0
        for ele in nums:
            res = res ^ ele
        temp = res & (-res)
        for ele in nums:
            if ele & temp:
                first ^= ele
            # 方法1: 分别计算两组的值
            # else:
            #     second ^= ele
        # 方法2: 通过first和res求出second的值
        second = res ^ first
        return [first, second]

    print(singleNumber([1,2,1,3,2,5]))
# leetcode submit region end(Prohibit modification and deletion)
