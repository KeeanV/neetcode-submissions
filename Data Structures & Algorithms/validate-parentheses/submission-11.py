class Solution:
    def isValid(self, s: str) -> bool:
       my_stack = []
       my_map = { ")" : "(", "]" : "[", "}" : "{"}
       for c in s:
        if c in my_map:
            if my_stack and my_stack[-1] == my_map[c]:
                my_stack.pop()
            else:
                return False
        else:
            my_stack.append(c)
       if my_stack:
        return False
       else:
        return True
