class Solution:

    def encode(self, strs: List[str]) -> str:
       result = ""
       for s in strs:
        length = str(len(s))
        result+=length + '#' + s
       return result




    def decode(self, s: str) -> List[str]:
       result = []
       i = 0
       while i < len(s):
        j = i
        while s[j] != '#':
            j+=1
        length = int(s[i:j])
        i = j + 1 # move i to start of string
        j = i + length # move j to next number
        result.append(s[i:j]) # append just the string
        i = j # i and j both at next number
       return result



