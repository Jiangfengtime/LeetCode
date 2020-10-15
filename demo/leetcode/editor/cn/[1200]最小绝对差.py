# 给你个整数数组 arr，其中每个元素都 不相同。 
# 
#  请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [4,2,1,3]
# 输出：[[1,2],[2,3],[3,4]]
#  
# 
#  示例 2： 
# 
#  输入：arr = [1,3,6,10,15]
# 输出：[[1,3]]
#  
# 
#  示例 3： 
# 
#  输入：arr = [3,8,-10,23,19,-4,-14,27]
# 输出：[[-14,-10],[19,23],[23,27]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= arr.length <= 10^5 
#  -10^6 <= arr[i] <= 10^6 
#  
#  Related Topics 数组 
#  👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_size = 200001
        result = []
        for index in range(len(arr) - 1):
            if arr[index + 1] - arr[index] < min_size:
                min_size = arr[index + 1] - arr[index]
                result.clear()
                result.append([arr[index], arr[index + 1]])
            elif arr[index + 1] - arr[index] == min_size:
                result.append([arr[index], arr[index + 1]])
        return result

    print(minimumAbsDifference([3,8,-10,23,19,-4,-14,27]))
        
# leetcode submit region end(Prohibit modification and deletion)
