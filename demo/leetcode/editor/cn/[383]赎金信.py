# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面
# 的字符构成。如果可以构成，返回 true ；否则返回 false。 
# 
#  (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。) 
# 
#  
# 
#  注意： 
# 
#  你可以假设两个字符串均只含有小写字母。 
# 
#  canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#  
#  Related Topics 字符串


# 一个很有启发的答案
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for ch in set(ransomNote):
#             if ransomNote.count(ch)>magazine.count(ch):
#                 return False
#         return True



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canConstruct(ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        list1 = []
        for ele in ransomNote:
            list1.append(ele)

        for elem in magazine:
            if elem in list1:
                list1.remove(elem)
        if not list1:
            return True
        else:
            return False

    print(canConstruct("we", "2we"))



# leetcode submit region end(Prohibit modification and deletion)
