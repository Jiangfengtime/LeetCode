# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 
# 
#  示例 1: 
# 
#  输入: num1 = "2", num2 = "3"
# 输出: "6" 
# 
#  示例 2: 
# 
#  输入: num1 = "123", num2 = "456"
# 输出: "56088" 
# 
#  说明： 
# 
#  
#  num1 和 num2 的长度小于110。 
#  num1 和 num2 只包含数字 0-9。 
#  num1 和 num2 均不以零开头，除非是数字 0 本身。 
#  不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。 
#  
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiply(num1: str, num2: str) -> str:
        # 方法一
        # len1 = len(num1)
        # len2 = len(num2)
        # result = 0
        # if not num1 or not num2:
        #     return "0"
        # for i in range(len1 - 1, -1, -1):
        #     for j in range(len2 - 1, -1, -1):
        #         num = int(num1[i]) * int(num2[j])
        #         flag = len1 + len2 - i - j - 2
        #         result = num * pow(10, flag) + result
        # return result

        # 方法二
        arr1 = list(num1)
        arr2 = list(num2)
        res = [0 for _ in range(len(arr1) + len(arr2))]
        for i in range(len(arr2) - 1, -1, -1):
            for j in range(len(arr1) - 1, -1, -1):
                temp = int(arr1[j]) * int(arr2[i])
                sum = temp + res[i + j + 1]
                res[i + j + 1] = sum % 10
                res[i + j] += sum // 10
        result = ""
        for ele in res:
            if ele != 0 or result:
                result += str(ele)
        return "0" if not result else result

    print(multiply("1244223423423343242431", "2442536545334565643"))


# leetcode submit region end(Prohibit modification and deletion)
