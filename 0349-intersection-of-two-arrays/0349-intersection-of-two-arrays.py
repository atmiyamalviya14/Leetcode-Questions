class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen = set(nums1)
        res = []
        for i in nums2:
            if i in seen:
                res.append(i)
                seen.remove(i)
        return res
        