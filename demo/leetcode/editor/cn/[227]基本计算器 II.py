# 实现一个基本的计算器来计算一个简单的字符串表达式的值。 
# 
#  字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格 。 整数除法仅保留整数部分。 
# 
#  示例 1: 
# 
#  输入: "3+2*2"
# 输出: 7
#  
# 
#  示例 2: 
# 
#  输入: " 3/2 "
# 输出: 1 
# 
#  示例 3: 
# 
#  输入: " 3+5 / 2 "
# 输出: 5
#  
# 
#  说明： 
# 
#  
#  你可以假设所给定的表达式都是有效的。 
#  请不要使用内置的库函数 eval。 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def calculate(s: str) -> int:
        num = 0
        stack = []
        sign = '+'
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                num = 10 * num + int(ch)
            if ch in "+-*/" or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = ch
        return sum(stack)



        # return list1

    print(calculate("-3/2"))



# leetcode submit region end(Prohibit modification and deletion)
