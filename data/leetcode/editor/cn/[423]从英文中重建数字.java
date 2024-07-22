/**
给你一个字符串 s ，其中包含字母顺序打乱的用英文单词表示的若干数字（0-9）。按 升序 返回原始的数字。 

 

 示例 1： 

 
输入：s = "owoztneoer"
输出："012"
 

 示例 2： 

 
输入：s = "fviefuro"
输出："45"
 

 

 提示： 

 
 1 <= s.length <= 10⁵ 
 s[i] 为 ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"] 这些字符之一 
 s 保证是一个符合题目要求的字符串 
 

 Related Topics 哈希表 数学 字符串 👍 213 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String originalDigits(String s) {
        int[] arr = new int[26];
        for (char cur: s.toCharArray()) {
            arr[cur - 'a']++;
        }
        StringBuilder sb = new StringBuilder();
        sb.append(helper(arr['z' - 'a'], "0"));
        sb.append(helper(arr['o' - 'a'] - arr['z' - 'a'] - arr['w' - 'a'] - arr['u' - 'a'], "1"));
        sb.append(helper(arr['w' - 'a'], "2"));
        sb.append(helper(arr['t' - 'a'] - arr['w' - 'a'] - arr['g' - 'a'], "3"));
        sb.append(helper(arr['u' - 'a'], "4"));
        sb.append(helper(arr['f' - 'a'] - arr['u' - 'a'], "5"));
        sb.append(helper(arr['x' - 'a'], "6"));
        sb.append(helper(arr['v' - 'a'] + arr['u' - 'a'] - arr['f' - 'a'], "7"));
        sb.append(helper(arr['g' - 'a'], "8"));
        sb.append(helper(arr['i' - 'a'] - arr['g' - 'a'] - arr['x' - 'a'] - arr['f' - 'a'] + arr['u' - 'a'], "9"));
        return sb.toString();

    }

    protected String helper(int num, String word) {
        if (num == 0) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < num; i++) {
            sb.append(word);
        }
        return sb.toString();
    }
}
//leetcode submit region end(Prohibit modification and deletion)
