# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def longestValidParentheses(s: str) -> int:
        size = len(s)
        # 存放所有"("的下标
        list1 = []
        max_len = 0
        len1 = 0
        # 标记出无法匹配的括号
        mark = [0 for _ in range(size)]
        for i in range(size):
            if s[i] == '(':
                list1.append(i)
            else:
                # 如果此时列表为空, 则")"无法匹配, 所以标记为1
                if not list1:
                    mark[i] = 1
                else: # 否则, 弹出与之相匹配的"("
                    list1.pop()
        # 此时list1中存放的元素, 即为未匹配的多余的"(", 标记为1
        while list1:
            mark[list1[-1]] = 1
            list1.pop()
        # 然后遍历mark获取所有的状态, 最长的连续0的长度即为最长有效括号的长度
        for i in range(size):
            # 如果遇到了不匹配的括号, 直接修改当前长度为0
            if mark[i]:
                len1 = 0
                continue
            len1 += 1
            max_len = max(max_len, len1)
        return max_len

    print(longestValidParentheses("()((()))"))
    # print(isValid("()()"))

# leetcode submit region end(Prohibit modification and deletion)
