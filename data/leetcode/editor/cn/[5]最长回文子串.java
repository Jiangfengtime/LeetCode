/**
给你一个字符串 s，找到 s 中最长的回文子串。 

 

 示例 1： 

 
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
 

 示例 2： 

 
输入：s = "cbbd"
输出："bb"
 

 

 提示： 

 
 1 <= s.length <= 1000 
 s 仅由数字和英文字母组成 
 

 Related Topics 字符串 动态规划 👍 5494 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        for (int i = 0; i < s.length(); i++) {
            String str1 = helper(s, i, i);
            String str2 = helper(s, i, i + 1);
            if (str1.length() > res.length()) {
                res = str1;
            }
            if (str2.length() > res.length()) {
                res = str2;
            }
        }
        return res;
    }

    private String helper(String s, int left, int right) {
        while (left >= 0 && right < s.length() &&
            s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return s.list(left + 1, right);
    }
}
//leetcode submit region end(Prohibit modification and deletion)
