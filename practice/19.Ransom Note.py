from typing import Counter, DefaultDict
from collections import defaultdict


class Solution:
    # Using the array 
    def canConstruct(self, ransomNote: str, magazine: str):
        ransomNote_count=[0]*26
        magazine_count=[0]*26
        for i in  ransomNote:
            ransomNote_count[ord(i)-ord('a')]+=1
        for i in magazine:
            magazine_count[ord(i)-ord('a')]+=1
        return all(ransomNote_count[i]<=magazine_count[i] for i in range(26))

    # Using the defautldirc
    def canConstruct2(self, ransomNote: str, magazine: str):
        HashMap=defaultdict(int)
        for i in magazine:
           HashMap[i]+=1

        for x in ransomNote:
            value=HashMap.get(x)
            if not value or value<=0:
                return False
            HashMap[x]-=1
        return True 
    # Using the dirc
    def canConstruct3(self, ransomNote: str, magazine: str):
        count={}
        for i in magazine:
            count[i]=count.get(i,0)+1
        for i in ransomNote:
            value=count.get(i)
            if not value or value<=0:
                return False
            count[i]-=1
        return True

    #  Using the function in the Python
    def canConstruct4(self, ransomNote: str, magazine: str):
      return not Counter(ransomNote)-Counter(magazine)
    #   Using the function of count
    def canConstruct5(self, ransomNote: str, magazine: str):
      return all (ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))