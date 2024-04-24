# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

from typing import List

# Brute Force:
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         maxNum = nums[0]
        
#         for i in range(len(nums)):
#             currMax = 0
#             for j in range(i, len(nums)):
#                 currMax += nums[j]
#                 maxNum = max(maxNum, currMax)
                
#         return maxNum
        

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxNum = nums[0]
        
        currMax = nums[0]
        for i in range(1, len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            maxNum = max(currMax, maxNum)
            
            
                
            
            maxNum = max(maxNum, currMax)
                
        return maxNum