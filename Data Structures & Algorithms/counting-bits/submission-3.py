class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(0,n+1):
            total = bin(i).count('1')
            output.append(total)
        return output