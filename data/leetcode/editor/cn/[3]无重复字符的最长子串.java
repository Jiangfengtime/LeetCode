/**
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 

 

 示例 1: 

 
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 

 示例 2: 

 
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 

 示例 3: 

 
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 

 

 提示： 

 
 0 <= s.length <= 5 * 10⁴ 
 s 由英文字母、数字、符号和空格组成 
 

 Related Topics 哈希表 字符串 滑动窗口 👍 7889 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int lengthOfLongestSubstring(String s) {

        Set<Character> set = new HashSet<>();
        int ans = 0;
        int left = 0, right = 0, size = s.length();
        while(right < size) {
            char cur = s.charAt(right);
            if(set.contains(cur)) {
                char ele = s.charAt(left);
                while(ele != cur) {
                    left++;
                    set.remove(ele);
                    ele = s.charAt(left);
                }
                left++;
                set.remove(ele);
            }
            set.add(cur);
            right++;
            ans = Math.max(right - left , ans);
        }
        return ans;


    }
}
//leetcode submit region end(Prohibit modification and deletion)
