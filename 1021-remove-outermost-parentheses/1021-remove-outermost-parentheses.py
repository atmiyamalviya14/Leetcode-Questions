class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0 
        output = ""
        for ch in s:
            if ch == "(":
                count +=1
                if count >1:
                    output+= ch
            else :
                count -=1
                if count>0:
                    output+=ch
        return output
