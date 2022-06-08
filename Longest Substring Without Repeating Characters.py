'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        logest_sub_word=''
        if len(s)<0 or len(s)>5*10**4 or s=="":return 0
        if len(s)==1:return 1
        result=0
        for i in s:
            if i not in logest_sub_word:
                logest_sub_word+=i
                if len(logest_sub_word)>result:
                    result=len(logest_sub_word)
            else:
                logest_sub_word=logest_sub_word.split(i)[1]
                logest_sub_word+=i
        return result