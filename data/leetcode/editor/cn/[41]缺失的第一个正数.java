/**
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。 请你实现时间复杂度为 
O(n) 并且只使用常数级别额外空间的解决方案。

 

 示例 1： 

 
输入：nums = [1,2,0]
输出：3
 

 示例 2： 

 
输入：nums = [3,4,-1,1]
输出：2
 

 示例 3： 

 
输入：nums = [7,8,9,11,12]
输出：1
 

 

 提示： 

 
 1 <= nums.length <= 5 * 10⁵ 
 -2³¹ <= nums[i] <= 2³¹ - 1 
 

 Related Topics 数组 哈希表 👍 1723 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int firstMissingPositive(int[] nums) {
        // 如果长度为n，最大的返回值是n+1，大于n+1的值一定不可能是返回值
        int size = nums.length;
        for (int i = 0; i < size; i++) {
            if (nums[i] <= 0) {
                nums[i] = size + 1;
            }
        }
        for(int i = 0; i < size; i++) {
            int cur = Math.abs(nums[i]);
            if (cur <= size) {
                nums[cur - 1] = - Math.abs(nums[cur - 1]);
            }
        }
        for(int i = 0; i < size; i++) {
            if(nums[i] >= 0) {
                return i + 1;
            }
        }
        return size + 1;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
