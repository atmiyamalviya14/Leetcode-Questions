class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def getString(string):
            stack=[]
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            
            return stack
        return getString(s) == getString(t)
