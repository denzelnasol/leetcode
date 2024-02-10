class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        availableLetters = {}
        for letter in magazine:
            if letter not in availableLetters:
                availableLetters[letter] = 0
            availableLetters[letter] += 1
            
        for letter in ransomNote:
            if letter not in availableLetters:
                return False
            availableLetters[letter] -= 1
            
        for num in availableLetters.values():
            if num < 0:
                return False
            
        return True