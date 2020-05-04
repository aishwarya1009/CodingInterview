class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        output = 0
        jewel_set = set(J)
        for char in S:
            if char in jewel_set:
                output += 1

        return output