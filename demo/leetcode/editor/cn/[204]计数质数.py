# 统计所有小于非负整数 n 的质数的数量。 
# 
#  示例: 
# 
#  输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#  
#  Related Topics 哈希表 数学 
#  👍 414 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def countPrimes(n: int) -> int:
        if n < 2:
            return 0
        result = [1] * n
        result[0] = result[1] = 0
        for ele in range(int(math.sqrt(n)) + 1):
            if result[ele] == 1:
                for e in range(ele * ele, n, ele):
                    result[e] = 0
                # result[ele * ele: n: ele] = [0] * ((n - 1 - ele * ele) // ele + 1)
        return sum(result)

    print(countPrimes(30))


# leetcode submit region end(Prohibit modification and deletion)
