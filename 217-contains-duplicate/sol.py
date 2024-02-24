# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()
        for num in nums:
            if num in numSet:
                return True
            
            numSet.add(num)
                
        return False