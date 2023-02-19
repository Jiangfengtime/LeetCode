/**
给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。 

 

 示例 1： 

 
输入：nums = [1,2,3]
输出：6
 

 示例 2： 

 
输入：nums = [1,2,3,4]
输出：24
 

 示例 3： 

 
输入：nums = [-1,-2,-3]
输出：-6
 

 

 提示： 

 
 3 <= nums.length <= 10⁴ 
 -1000 <= nums[i] <= 1000 
 

 Related Topics 数组 数学 排序 👍 423 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int maximumProduct(int[] nums) {
        int res = Integer.MIN_VALUE, size = nums.length;
        Arrays.sort(nums);
        // 全正或全负都是值越大越好
        res = Math.max(res, nums[size - 3] * nums[size - 2] * nums[size - 1]);
        // 两负一正，正数越大越好，负数越小越好
        res = Math.max(res, nums[0] * nums[1] * nums[size - 1]);

        return res;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
