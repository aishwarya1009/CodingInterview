from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        for char in ransomNote:
            if char in mag_count and mag_count[char] > 0:
                mag_count[char] -= 1
            else:
                return False
        return True