/**
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。 

 

 示例 1： 

 
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
 

 示例 2: 

 
输入：nums = [1,0,1,1,0,1]
输出：2
 

 

 提示： 

 
 1 <= nums.length <= 10⁵ 
 nums[i] 不是 0 就是 1. 
 

 Related Topics 数组 👍 366 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int res = 0;
        int tmp = 0;
        for(int cur: nums) {
            if (cur == 1) {
                tmp++;
                res = Math.max(res, tmp);
            } else {
                tmp = 0;
            }
        }
        return res;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
