# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。 
# 
#  案例: 
# 
#  
# s = "leetcode"
# 返回 0.
# 
# s = "loveleetcode",
# 返回 2.
#  
# 
#  
# 
#  注意事项：您可以假定该字符串只包含小写字母。 
#  Related Topics 哈希表 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i

    print(firstUniqChar("asesa"))
# leetcode submit region end(Prohibit modification and deletion)
