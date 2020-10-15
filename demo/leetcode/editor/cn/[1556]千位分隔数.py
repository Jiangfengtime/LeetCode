# 给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 987
# 输出："987"
#  
# 
#  示例 2： 
# 
#  输入：n = 1234
# 输出："1.234"
#  
# 
#  示例 3： 
# 
#  输入：n = 123456789
# 输出："123.456.789"
#  
# 
#  示例 4： 
# 
#  输入：n = 0
# 输出："0"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n < 2^31 
#  
#  Related Topics 字符串 
#  👍 1 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def thousandSeparator(n: int) -> str:
        arr = []
        res = ""
        if n == 0:
            return "0"
        while n > 0:
            arr.append(str(n % 1000))
            n //= 1000
        res += arr[len(arr) - 1] + "."
        for i in range(len(arr) - 2, -1, -1):
            res += arr[i].zfill(3) + "."

        return res[:-1]



    print(thousandSeparator(0))
# leetcode submit region end(Prohibit modification and deletion)
