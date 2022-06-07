'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        LongestCommonPrefix = ""
        if len(strs) == 0: return ""
        if len(strs) == 1 : return strs[0]
        index = 0
        strs.sort()
        
        minimum_lenght = min(len(strs[0]), len(strs[len(strs)-1]))
        
        while index < minimum_lenght:
            
            if strs[0][index]  == strs[ len(strs) - 1 ][index]:
                
                LongestCommonPrefix += strs[0][index]
            else:
                break
            
            index+=1
        
        return LongestCommonPrefix
                      