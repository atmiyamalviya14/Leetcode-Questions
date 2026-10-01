class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_nums = set()
        for num in nums:
            if num in set_nums:
                return True
            set_nums.add(num)
        return False
