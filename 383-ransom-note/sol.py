class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): return False
        
        availableLetters = {}
        for letter in magazine:
            if letter not in availableLetters:
                availableLetters[letter] = 0
            availableLetters[letter] += 1
            
        for letter in ransomNote:
            if letter not in availableLetters or availableLetters[letter] == 0:
                return False
            availableLetters[letter] -= 1
            
            
        return True