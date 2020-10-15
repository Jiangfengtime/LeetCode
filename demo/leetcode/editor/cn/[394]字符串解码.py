# 给定一个经过编码的字符串，返回它解码后的字符串。 
# 
#  编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。 
# 
#  你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。 
# 
#  此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "3[a]2[bc]"
# 输出："aaabcbc"
#  
# 
#  示例 2： 
# 
#  输入：s = "3[a2[c]]"
# 输出："accaccacc"
#  
# 
#  示例 3： 
# 
#  输入：s = "2[abc]3[cd]ef"
# 输出："abcabccdcdcdef"
#  
# 
#  示例 4： 
# 
#  输入：s = "abc3[cd]xyz"
# 输出："abccdcdcdxyz"
#  
#  Related Topics 栈 深度优先搜索 
#  👍 466 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(s: str) -> str:
        stack_num = []
        stack_char = []
        arr = list(s)
        temp = 0
        index = 0
        size = len(arr)
        res = ""
        str = "0123456789"
        while index < size:
            while arr[index] in str:
                temp = 10 * temp + int(arr[index])
                index += 1
            if arr[index] == "[":
                stack_num.append(temp)
                stack_char.append(index)
                temp = 0
            if arr[index] == "]":
                arr[stack_char[-1] - 1: index + 1] = arr[stack_char[-1] + 1: index] * stack_num[-1]
                index = stack_char[-1] - 1
                stack_num.pop()
                stack_char.pop()
            index += 1
            size = len(arr)
        for ele in arr:
            if ele not in str:
                res += ele

        return res


    print(decodeString("2[10[bc]10[xy]][a]"))

# leetcode submit region end(Prohibit modification and deletion)
