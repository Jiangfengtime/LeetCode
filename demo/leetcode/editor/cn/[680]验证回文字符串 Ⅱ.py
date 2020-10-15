# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  示例 1: 
# 
#  
# 输入: "aba"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#  
# 
#  注意: 
# 
#  
#  字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
def huiwen(str1):
    for i in range(int(len(str1) / 2)):
        if str1[i] != str1[len(str1) - 1 - i]:
            return False
    return True


class Solution(object):
    def validPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return huiwen(s[i:j]) | huiwen(s[i + 1: j + 1])
            else:
                i += 1
                j -= 1
        return True



    print(validPalindrome("abca"))


        
# leetcode submit region end(Prohibit modification and deletion)
