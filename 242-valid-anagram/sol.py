from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = defaultdict(int)
        for c in t:
            letterMap[c] += 1

        for c in s:
            letterMap[c] -= 1

        for num in letterMap.values():
            if num != 0:
                return False
            
        return True