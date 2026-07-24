class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #initialize a stack, just an empty list.
        dikt = { ")":"(", "]":"[", "}":"{"} #define a hashmap w/ key + values

        for i in s: #go through every char in the string
            if i in dikt:   #if we come across a closing bracket
                if stack and stack[-1] == dikt[i]:  # check that the stack isnt empty cuz cant start w closing, and check that the previous entry in the stack is the corresponding open bracket.
                    stack.pop()     #remove that closing from the stack
                else:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        else:
             return False