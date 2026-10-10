class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_sum  = 0 
        curr_sum = 0 
        for i in range(len(gain)):
            curr_sum += gain[i] 
            max_sum = max(max_sum , curr_sum)
        return max_sum