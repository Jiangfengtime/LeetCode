# 给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字
# 符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。 
# 
#  示例： 
# 
#  输入：
# big = "mississippi"
# smalls = ["is","ppi","hi","sis","i","ssippi"]
# 输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
#  
# 
#  提示： 
# 
#  
#  0 <= len(big) <= 1000 
#  0 <= len(smalls[i]) <= 1000 
#  smalls的总字符数不会超过 100000。 
#  你可以认为smalls中没有重复字符串。 
#  所有出现的字符均为英文小写字母。 
#  
#  Related Topics 字典树 字符串 
#  👍 12 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
# leetcode submit region end(Prohibit modification and deletion)
