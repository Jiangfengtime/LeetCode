/**
给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 

 

 示例 1： 

 
输入：timePoints = ["23:59","00:00"]
输出：1
 

 示例 2： 

 
输入：timePoints = ["00:00","23:59","00:00"]
输出：0
 

 

 提示： 

 
 2 <= timePoints.length <= 2 * 10⁴ 
 timePoints[i] 格式为 "HH:MM" 
 

 Related Topics 数组 数学 字符串 排序 👍 262 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public int findMinDifference(List<String> timePoints) {
        int[] res = new int[timePoints.size() * 2];
        int idx = 0;
        for (String str: timePoints) {
            String[] arr = str.split("\\:");
            int tmp = Integer.parseInt(arr[0]) * 60 + Integer.parseInt(arr[1]);
            res[idx++] = tmp;
            res[idx++] = tmp + 60 * 24;
        }
        int ans = 60 * 12;
        Arrays.sort(res);
        for (int i = 0; i < res.length - 1; i++) {
            ans = Math.min(ans, res[i + 1] - res[i]);
        }
        return ans;

    }
}
//leetcode submit region end(Prohibit modification and deletion)
