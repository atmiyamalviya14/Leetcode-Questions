class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        c1 = [0]*26
        c2 = [0]*26

        for ch in s1:
            c1[ord(ch) - ord('a')] += 1 
        
        left = 0 

        for right in range(len(s2)):
            c2[ord(s2[right])- ord('a')] += 1

            if right - left + 1 > len(s1):
                c2[ord(s2[left]) - ord('a')] -=1 
                left +=1 

            if c1 == c2:
                return True
        return False

