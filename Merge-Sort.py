
'''
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums)==1:
                return
            center_index = len(nums)//2
            left_half = nums[:center_index]
            right_half = nums[center_index:]

            merge_sort(left_half)
            merge_sort(right_half)

            left_half_index=0
            right_half_index=0
            final_result_index=0

            while left_half_index <len(left_half) and right_half_index<len(right_half):
                
                if left_half[left_half_index]<right_half[right_half_index]:
                    nums[final_result_index] = left_half[left_half_index]
                    left_half_index+=1
                    final_result_index+=1
                    
                else:
                    nums[final_result_index]=right_half[right_half_index]
                    right_half_index+=1
                    final_result_index+=1
                    
            while left_half_index < len(left_half):
                nums[final_result_index]=left_half[left_half_index]
                final_result_index+=1
                left_half_index+=1
                
            while right_half_index < len(right_half):
                nums[final_result_index]=right_half[right_half_index]
                right_half_index+=1
                final_result_index+=1
                
        merge_sort(nums)
        return nums