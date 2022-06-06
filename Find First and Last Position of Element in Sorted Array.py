'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index , last_index = 0 , len(nums)
        first_visit , second_visit = -1,-1
        if len(nums)==0:
            return [-1,-1]
        
        while start_index<last_index:
            
            center_index = (start_index+last_index)//2
            
            if target <= nums[center_index]:
                last_index = center_index
            else:
                start_index = center_index+1
                
        if start_index < len(nums) and target == nums[start_index]:
            first_visit = start_index
            
        start_index , last_index = 0 , len(nums)
        
        while start_index < last_index:
            
            center_index = (start_index+last_index)//2
            
            if target >= nums[center_index]:
                start_index = center_index+1
            else:
                last_index = center_index
                
        if target==nums[last_index-1]:
            second_visit = last_index-1
            
        return [first_visit,second_visit]

