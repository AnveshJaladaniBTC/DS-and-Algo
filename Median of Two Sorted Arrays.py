'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged_list = nums1+nums2
    
        merged_list.sort()

        lenght_of_merged_list = len(merged_list)

        if lenght_of_merged_list % 2 == 0:

            centre = lenght_of_merged_list // 2
            return ( merged_list[centre] + merged_list[centre-1] ) / 2
        
        else:
            
            centre = lenght_of_merged_list // 2

            return float(merged_list[centre])