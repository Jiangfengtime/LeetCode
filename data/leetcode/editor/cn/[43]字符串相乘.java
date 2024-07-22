/**
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 

 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。 

 

 示例 1: 

 
输入: num1 = "2", num2 = "3"
输出: "6" 

 示例 2: 

 
输入: num1 = "123", num2 = "456"
输出: "56088" 

 

 提示： 

 
 1 <= num1.length, num2.length <= 200 
 num1 和 num2 只能由数字组成。 
 num1 和 num2 都不包含任何前导零，除了数字0本身。 
 

 Related Topics 数学 字符串 模拟 👍 1352 👎 0

*/

//leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public String multiply(String num1, String num2) {
        int size1 = num1.length(), size2 = num2.length();
        int tmp = 0;
        StringBuilder sb = new StringBuilder();
        int[] arr = new int[size1 + size2];
        for (int i = size1 - 1; i >= 0; i--) {
            for (int j = size2 - 1; j >= 0; j--) {
                int v1 = num1.charAt(i) - '0';
                int v2 = num2.charAt(j) - '0';
                int val = v1 * v2 + arr[i + j + 1];
                arr[i + j + 1] = val % 10;
                arr[i + j] += val / 10;
            }
        }

        for (int i = 0; i < size1 + size2; i++) {
            if (arr[i] != 0 || sb.length() != 0) {
                sb.append(arr[i]);
            }
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
//leetcode submit region end(Prohibit modification and deletion)
