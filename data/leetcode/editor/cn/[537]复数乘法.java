/**
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件： 

 
 实部 是一个整数，取值范围是 [-100, 100] 
 虚部 也是一个整数，取值范围是 [-100, 100] 
 i² == -1 
 

 给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。 

 

 示例 1： 

 
输入：num1 = "1+1i", num2 = "1+1i"
输出："0+2i"
解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
 

 示例 2： 

 
输入：num1 = "1+-1i", num2 = "1+-1i"
输出："0+-2i"
解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
 

 

 提示： 

 
 num1 和 num2 都是有效的复数表示。 
 

 Related Topics 数学 字符串 模拟 👍 158 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        String[] arr1 = num1.split("\\+|i");
        String[] arr2 = num2.split("\\+|i");
        // 实部：
        int v1 = Integer.parseInt(arr1[0]);
        int i1 = Integer.parseInt(arr1[1]);
        int v2 = Integer.parseInt(arr2[0]);
        int i2 = Integer.parseInt(arr2[1]);
        int sum1 = v1 * v2 - i1 * i2;
        int sum2 = v1 * i2 + v2 * i1;
        return sum1 + "+" + sum2 + "i";

    }
}
//leetcode submit region end(Prohibit modification and deletion)
