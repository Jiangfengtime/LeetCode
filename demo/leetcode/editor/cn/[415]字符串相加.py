# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。 
# 
#  注意： 
# 
#  
#  num1 和num2 的长度都小于 5100. 
#  num1 和num2 都只包含数字 0-9. 
#  num1 和num2 都不包含任何前导零。 
#  你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)
        num = ""
        num3 = ""
        i = j = min(len1, len2)
        flag = 0
        while i > 0:
            n1 = int(num1[len1 - 1])
            n2 = int(num2[len2 - 1])
            n3 = n1 + n2 + flag
            flag = 0
            if n3 < 10:
                num = str(n3) + num
            else:
                num = str(n3 % 10) + num
                flag = 1
            len1 -= 1
            len2 -= 1
            i -= 1
        if len1 > len2:
            num3 = int(num1[:-j]) + flag
        elif len2 > len1:
            num3 = int(num2[:-j]) + flag
        else:
            if flag == 1:
                num3 = flag
        return str(num3) + num

        # "6796423"
        # "253276"

    print(addStrings("6796423", "2523276"))


        
# leetcode submit region end(Prohibit modification and deletion)
