# 不使用运算符 + 和 - ，计算两整数 a 、b 之和。 
# 
#  示例 1: 
# 
#  输入: a = 1, b = 2
# 输出: 3
#  
# 
#  示例 2: 
# 
#  输入: a = -2, b = 3
# 输出: 1 
#  Related Topics 位运算 
#  👍 296 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getSum(a: int, b: int) -> int:
        num1 = a if a >= 0 else ~a + 1
        num2 = b if b >= 0 else ~b + 1




    print(getSum(-11, 6))
        
# leetcode submit region end(Prohibit modification and deletion)
