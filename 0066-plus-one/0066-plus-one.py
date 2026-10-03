class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''.join(map(str,digits))
        s = int(s)
        s = s+1
        s = str(s)
        return [int(x) for x in s]