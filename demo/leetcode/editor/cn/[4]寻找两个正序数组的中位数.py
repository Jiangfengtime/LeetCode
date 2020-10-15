# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
# 
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]):
        len1 = len(nums1)
        len2 = len(nums2)
        size = len1 + len2
        # left 用于存放遍历的前一个值
        # right 用于存放遍历的当前值
        left, right = -1, -1
        # aStart, bStart 用于表示指针的移动
        aStart, bStart = 0, 0
        # 只需要遍历 size/2 + 1次就遍历到中位数了
        for num in range(size // 2 + 1):
            # 每一次循环, 就将当前的值赋值给前一个值
            left = right

            # 当nums1还没有遍历到最后, 且
            # aStart指向的值小于bStart执行的值 或者 nums2已经遍历到最后了
            # 此时就移动nums1
            if aStart < len1 and (bStart >= len2 or nums1[aStart] < nums2[bStart]):
                right = nums1[aStart]
                aStart += 1
            # 否则就移动nums2
            else:
                right = nums2[bStart]
                bStart += 1
        # 如果列表长度和为偶数, 则中位数是中间两个数之和再求平均
        if size % 2 == 0:
            return (left + right) / 2
        # 如果类别长度为奇数, 则中位数是最中间的那个数
        else:
            return right

    print(findMedianSortedArrays([1, 3, 5], [-1, 2, 3]))
