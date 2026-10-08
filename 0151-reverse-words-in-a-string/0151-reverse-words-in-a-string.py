class Solution:
    def reverseWords(self, s: str) -> str:
        if s is None:
            return s
        words=s.split()
        reverse=words[::-1]
        output = ""
        for word in reverse:
            output +=  word + " "
        return output.strip() 

        