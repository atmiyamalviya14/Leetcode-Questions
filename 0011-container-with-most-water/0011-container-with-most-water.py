class Solution:
    def maxArea(self, height: list[int]) -> int:
        beg = 0 
        end = len(height) -1
        max_area = 0 
        while beg < end:
            max_area = max(min(height[beg],height[end])*(end-beg), max_area)
            if height[beg] < height[end]:
                beg+=1
            else:
                end-=1
        return max_area