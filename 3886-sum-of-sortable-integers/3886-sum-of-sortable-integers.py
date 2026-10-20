class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            sortable = True
            prev_max = float("-inf")

            for i in range(0, n, k):
                block = nums[i:i + k]
                m = len(block)

                # Check whether this block can be sorted by rotation
                descents = 0

                for j in range(m):
                    if block[j] > block[(j + 1) % m]:
                        descents += 1

                if descents > 1:
                    sortable = False
                    break

                # Check whether sorted blocks form a sorted array
                if prev_max > min(block):
                    sortable = False
                    break

                prev_max = max(block)

            if sortable:
                ans += k

        return ans
