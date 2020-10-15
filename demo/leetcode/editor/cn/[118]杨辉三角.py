# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。 
# 
#  
# 
#  在杨辉三角中，每个数是它左上方和右上方的数的和。 
# 
#  示例: 
# 
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ] 
#  Related Topics 数组 
#  👍 336 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generate(numRows: int) -> List[List[int]]:
        arr = [[0 for _ in range(_ + 1)] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if i == j or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
        return arr

    print(generate(5))

# leetcode submit region end(Prohibit modification and deletion)
