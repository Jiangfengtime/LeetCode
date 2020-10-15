# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。 
# 
#  
# 
#  
# 
#  
# 
#  示例： 
# 
#  输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
#  
# 
#  
# 
#  注意： 
# 
#  
#  你可以重复使用键盘上同一字符。 
#  你可以假设输入的字符串将只包含字母。 
#  Related Topics 哈希表 
#  👍 103 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        result = []
        for word in words:
            setx = set(word.lower())
            if setx <= set1 or setx <= set2 or setx <= set3:
                result.append(word)

        return result
    print()
# leetcode submit region end(Prohibit modification and deletion)
