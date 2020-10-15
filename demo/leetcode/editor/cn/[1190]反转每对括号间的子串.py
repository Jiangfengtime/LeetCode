# 给出一个字符串 s（仅含有小写英文字母和括号）。 
# 
#  请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。 
# 
#  注意，您的结果中 不应 包含任何括号。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "(abcd)"
# 输出："dcba"
#  
# 
#  示例 2： 
# 
#  输入：s = "(u(love)i)"
# 输出："iloveu"
#  
# 
#  示例 3： 
# 
#  输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
#  
# 
#  示例 4： 
# 
#  输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 2000 
#  s 中只有小写英文字母和括号 
#  我们确保所有括号都是成对出现的 
#  
#  Related Topics 栈 
#  👍 40 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseParentheses(s: str):
        # 方法一: 暴力法
        # arr = list(s)
        # stack = []
        # res = ""
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         stack.append(i)
        #     elif s[i] == ")":
        #         arr[stack[-1] + 1: i] = arr[i - 1:stack[-1]: -1]
        #         stack.pop()
        # for ele in arr:
        #     if ele != "(" and ele != ")":
        #         res += ele
        #
        # return res

        # 方法二: 虫洞法
        stack, arr = [], [-1] * len(s)
        flag, size, index = 1, 0, 0
        res = ""
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                arr[i] = stack[-1]
                arr[stack[-1]] = i
                stack.pop()
        while size < len(s):
            if s[index] == "(" or s[index] == ")":
                flag = - flag
                index = arr[index] + flag
            else:
                res += s[index]
                index += flag
            size += 1
        return res

    print(reverseParentheses("(u(love)i)"))

        
# leetcode submit region end(Prohibit modification and deletion)
