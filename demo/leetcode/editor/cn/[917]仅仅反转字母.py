# 给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入："ab-cd"
# 输出："dc-ba"
#  
# 
#  示例 2： 
# 
#  输入："a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#  
# 
#  示例 3： 
# 
#  输入："Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#  
# 
#  
# 
#  提示： 
# 
#  
#  S.length <= 100 
#  33 <= S[i].ASCIIcode <= 122 
#  S 中不包含 \ or " 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseOnlyLetters( S: str) -> str:
        if not S.isalpha():
            return S

        list1 = list(S)
        left = 0
        right = len(list1) - 1
        while left < right:
            while not list1[left].isalpha():
                left += 1
            while not list1[right].isalpha():
                right -= 1
            temp = list1[right]
            list1[right] = list1[left]
            list1[left] = temp
            left += 1
            right -= 1
        return "".join(list1)

    print(reverseOnlyLetters("ab_cd"))
        
# leetcode submit region end(Prohibit modification and deletion)
