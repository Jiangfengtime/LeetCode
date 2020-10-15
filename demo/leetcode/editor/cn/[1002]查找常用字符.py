# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  输入：["bella","label","roller"]
# 输出：["e","l","l"]
#  
# 
#  示例 2： 
# 
#  输入：["cool","lock","cook"]
# 输出：["c","o"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 100 
#  1 <= A[i].length <= 100 
#  A[i][j] 是小写字母 
#  
#  Related Topics 数组 哈希表 
#  👍 87 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List

import collection as collection


class Solution:
    def commonChars(A: List[str]) -> List[str]:
        result = []
        arr_map = collections.Counter(A[0])
        for ele in A:
            ele_map = collections.Counter(ele)

            for key in arr_map.keys():
                if key not in ele_map:
                    arr_map[key] = 0
                else:
                    arr_map[key] = min(arr_map[key], ele_map[key])
        for key in arr_map:
            result += [key] * arr_map[key]
        return result

    print(commonChars(["bella", "label", "roller"]))
        
# leetcode submit region end(Prohibit modification and deletion)
