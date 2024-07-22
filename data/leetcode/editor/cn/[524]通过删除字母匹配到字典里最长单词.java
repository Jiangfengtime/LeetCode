/**
给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。 

 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。 

 

 示例 1： 

 
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"
 

 示例 2： 

 
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"
 

 

 提示： 

 
 1 <= s.length <= 1000 
 1 <= dictionary.length <= 1000 
 1 <= dictionary[i].length <= 1000 
 s 和 dictionary[i] 仅由小写英文字母组成 
 

 Related Topics 数组 双指针 字符串 排序 👍 371 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String findLongestWord(String s, List<String> dictionary) {
        int size = s.length();
        String res = "";
        for (String str: dictionary) {
            int len = str.length();
            int idx1 = 0, idx2 = 0;
            while (idx1 < size && idx2 < len) {
                if (s.charAt(idx1) == str.charAt(idx2)) {
                    idx2++;
                }
                idx1++;
            }
            if (idx2 == len && (res.length() < idx2 || res.length() == idx2 && res.compareTo(str) > 0)) {{
                    res = str;
                }
            }
        }
        return res;

    }

}
//leetcode submit region end(Prohibit modification and deletion)
