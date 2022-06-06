'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size_array = len(nums)
        start = 0
        last = size_array-1
        while start<last:
            center_index = int((start+last)/2)
            if nums[center_index] > nums[last]:
                start = center_index + 1
            else:
                last = center_index
        rotated_at = start
        
        start = 0
        last = len(nums)-1
        while start<=last:
            center_index = (start+last)//2
            center_index2 = (center_index+rotated_at)%size_array 
            if nums[center_index2]==target:
                return center_index2
            elif nums[center_index2] <target:
                start = center_index + 1
            else:
                last = center_index - 1
            
        return -1