# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。 
# 
#  有效字符串需满足： 
# 
#  
#  左括号必须用相同类型的右括号闭合。 
#  左括号必须以正确的顺序闭合。 
#  
# 
#  注意空字符串可被认为是有效字符串。 
# 
#  示例 1: 
# 
#  输入: "()"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: "()[]{}"
# 输出: true
#  
# 
#  示例 3: 
# 
#  输入: "(]"
# 输出: false
#  
# 
#  示例 4: 
# 
#  输入: "([)]"
# 输出: false
#  
# 
#  示例 5: 
# 
#  输入: "{[]}"
# 输出: true 
#  Related Topics 栈 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list1 = []
        for ele in s:
            if ele == "(" or ele == "[" or ele == "{":
                list1.append(ele)
            if not list1:
                return False
            elif ele == ")":
                if list1[-1] == "(":
                    list1.pop(-1)
                else:
                    return False
            elif ele == "]":
                if list1[-1] == "[":
                    list1.pop(-1)
                else:
                    return False
            elif ele == "}":
                if list1[-1] == "{":
                    list1.pop(-1)
                else:
                    return False
        if not list1:
            return True
        else:
            return False








        # list1 = []
        # for i in range(len(s)):
        #     # 如果是左括号, 则依次放入列表
        #     if s[i] == '{' or s[i] == '[' or s[i] == '(':
        #         list1.append(s[i])
        #     # 如果列表不为空, 且输入的是又括号
        #     elif len(list1) > 0:
        #         # 输入的右括号恰好和最后一个元素相匹配, 则弹出最后一个括号, 否则直接返回false
        #         if s[i] == '}' and list1[-1] == '{':
        #             list1.pop()
        #         elif s[i] == ']' and list1[-1] == '[':
        #             list1.pop()
        #         elif s[i] == ')' and list1[-1] == '(':
        #             list1.pop()
        #         else:
        #             return False
        #     # 如果列表为空, 还继续插入右括号
        #     else:
        #         return False
        # # 字符串遍历完成后, 列表如果不为空, 则返回false
        # if not list1:
        #     return True
        # else:
        #     return False












# leetcode submit region end(Prohibit modification and deletion)
