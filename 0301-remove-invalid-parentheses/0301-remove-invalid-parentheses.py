class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        left_remove = 0
        right_remove = 0

        # Find minimum removals needed
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, path, balance, left_remove, right_remove):

            # Invalid
            if balance < 0:
                return

            # Reached end
            if index == len(s):
                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            # Letter
            if ch.isalpha():
                path.append(ch)

                backtrack(
                    index + 1,
                    path,
                    balance,
                    left_remove,
                    right_remove
                )

                path.pop()

            # '('
            elif ch == '(':

                # Option 1: Remove it
                if left_remove > 0:
                    backtrack(
                        index + 1,
                        path,
                        balance,
                        left_remove - 1,
                        right_remove
                    )

                # Option 2: Keep it
                path.append('(')

                backtrack(
                    index + 1,
                    path,
                    balance + 1,
                    left_remove,
                    right_remove
                )

                path.pop()

            # ')'
            else:

                # Option 1: Remove it
                if right_remove > 0:
                    backtrack(
                        index + 1,
                        path,
                        balance,
                        left_remove,
                        right_remove - 1
                    )

                # Option 2: Keep it
                if balance > 0:
                    path.append(')')

                    backtrack(
                        index + 1,
                        path,
                        balance - 1,
                        left_remove,
                        right_remove
                    )

                    path.pop()

        backtrack(0, [], 0, left_remove, right_remove)

        return list(result)