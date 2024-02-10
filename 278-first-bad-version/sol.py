# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        middle = n // 2
        while left < right:
            if isBadVersion(middle):
                right = middle
            else:
                left = middle + 1
                
            middle = (left + right) // 2
        return left
    
    
    # 1, 2, 3