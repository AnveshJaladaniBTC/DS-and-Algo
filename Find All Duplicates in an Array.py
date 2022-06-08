'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dictionary_of_count = {}
        result =[]
        for i in nums:
            if i in dictionary_of_count:
                dictionary_of_count[i]+=1
            else:
                dictionary_of_count[i] = 1
        for i in dictionary_of_count:
            if dictionary_of_count[i]>1:
                result.append(i)
        return result
            
        