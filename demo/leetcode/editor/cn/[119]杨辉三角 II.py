# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 3
# 输出: [1,3,3,1]
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(k) 空间复杂度吗？ 
#  Related Topics 数组 
#  👍 166 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:


    def getRow(rowIndex: int) -> List[int]:
        result = [1 for _ in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1, i):
                index = i - j
                result[index] += result[index - 1]
        return result

    print(getRow(4))
# leetcode submit region end(Prohibit modification and deletion)
