'''
topic:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

'''

'''
train of though:
    we need to create an array to store the numbers of every words in the s, 
    Start traversal the t, when meet the number same in the t  will subtract the number in the array
    then traversal the array again, if ever number in the array is not 0 will return false
'''
class Solution:
    def isAnagram(self, s: str, t: str):
        record=[0]*26
        for i in  s:
            record[ord(i)-ord("a")]+=1
        for j in  t:
            record[ord(j)-ord("a")]-=1
        for i in range(26):
            if record[i] !=0:
                return False
        return True
