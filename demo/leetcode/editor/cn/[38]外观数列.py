# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下： 
# 
#  1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#  
# 
#  1 被读作 "one 1" ("一个一") , 即 11。 
# 11 被读作 "two 1s" ("两个一"）, 即 21。 
# 21 被读作 "one 2", "one 1" （"一个二" , "一个一") , 即 1211。 
# 
#  给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。 
# 
#  注意：整数序列中的每一项将表示为一个字符串。 
# 
#  
# 
#  示例 1: 
# 
#  输入: 1
# 输出: "1"
# 解释：这是一个基本样例。 
# 
#  示例 2: 
# 
#  输入: 4
# 输出: "1211"
# 解释：当 n = 3 时，序列是 "21"，其中我们有 "2" 和 "1" 两组，"2" 可以读作 "12"，也就是出现频次 = 1 而 值 = 2；类似 
# "1" 可以读作 "11"。所以答案是 "12" 和 "11" 组合在一起，也就是 "1211"。 
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def countAndSay(n: int) -> str:
        # 第一项的结果为"1"
        preItem = '1'
        # 计算下一项
        for i in range(1, n):
            # 初始化
            # 将num赋值为1, 下一项设置为空字符串, ele指向前一项的第一个元素
            num = 1
            nextItem = ""
            ele = preItem[0]
            # 遍历前一项的元素
            for j in range(1, len(preItem)):
                # 如果前一项和后一项的值相等, num + 1
                if ele == preItem[j]:
                    num += 1
                # 如果不相等, 进行字符串的拼接和num的初始化
                else:
                    # 将前一个元素的连续个数和值拼接成字符串
                    nextItem += str(num) + ele
                    # 将当前元素的值赋值给ele, 进行后续的比较
                    ele = preItem[j]
                    # 初始化num
                    num = 1
            # 拼接最后一项
            nextItem += str(num) + ele
            # 将后一项的值,赋值给前一项, 然后再循环
            preItem = nextItem
        return preItem

    print(countAndSay(6))

# leetcode submit region end(Prohibit modification and deletion)
