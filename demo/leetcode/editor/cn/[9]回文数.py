# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。 
# 
#  示例 1: 
# 
#  输入: 121
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#  
# 
#  示例 3: 
# 
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#  
# 
#  进阶: 
# 
#  你能不将整数转为字符串来解决这个问题吗？ 
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPalindrome(x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        num = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        if temp == num:
            return True
        else:
            return False


    print(isPalindrome(123121))
# leetcode submit region end(Prohibit modification and deletion)
