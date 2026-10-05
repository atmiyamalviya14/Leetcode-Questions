class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output = []
        for num in nums:
            ind = abs(num) - 1
            nums[ind]= -abs(nums[ind])

        for i in range(len(nums)):
            if nums[i] > 0:
                output.append(i+1)
        return output
