from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = Counter(s)
        for i,char in enumerate(s):
            if char_dict[char] == 1:
                return i
        return -1