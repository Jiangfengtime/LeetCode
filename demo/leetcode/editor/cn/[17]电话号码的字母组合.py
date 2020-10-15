# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  示例: 
# 
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#  
# 
#  说明: 
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。 
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        arr = [[], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"],
               ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],
               ["t", "u", "v"], ["w", "x", "y", "z"]]

        if not digits:
            return result

        i = int(digits[0])
        result = arr[i]
        for j in range(1, len(digits)):
            result = self.cartesian(result, arr[int(digits[j])])

        return result

    def cartesian(self, list1, list2):
        list3 = []
        for e1 in list1:
            for e2 in list2:
                ele = e1 + e2
                list3.append(ele)
        return list3
# leetcode submit region end(Prohibit modification and deletion)
