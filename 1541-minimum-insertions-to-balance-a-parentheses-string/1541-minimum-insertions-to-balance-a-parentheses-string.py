class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0  # Missing insertions
        need = 0   # Required closing parentheses

        for ch in s:
            if ch == '(':
                if need % 2 == 1:
                    count += 1
                    need -= 1

                need += 2

            else:
                need -= 1

                if need < 0:
                    count += 1
                    need = 1

        return count + need