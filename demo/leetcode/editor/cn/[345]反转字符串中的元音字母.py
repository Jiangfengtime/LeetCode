# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。 
# 
#  示例 1: 
# 
#  输入: "hello"
# 输出: "holle"
#  
# 
#  示例 2: 
# 
#  输入: "leetcode"
# 输出: "leotcede" 
# 
#  说明: 
# 元音字母不包含字母"y"。 
#  Related Topics 双指针 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(s: str):
        """
        :type s: str
        :rtype: str
        """
        temp = []
        flag = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ls = [i for i in s if i in flag]
        for ele in s:
            if ele not in flag:
                temp.append(ele)
            else:
                temp.append(ls.pop())
        # join(): 连接字符串数组. 将字符串、元组、列表中的元素
        # 以指定的字符(分隔符)连接生成一个新的字符串
        return "".join(temp)

    print(reverseVowels("abcde"))


