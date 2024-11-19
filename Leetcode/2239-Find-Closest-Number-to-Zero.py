class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        closest = nums[0]   # initialisation

        for x in nums:                  # looping over array
            if abs(x) < abs(closest):   # if we find even smaller number 
                closest = x             # than that number will be closest. 
        
        # if closest is negative and its absolute value (i.e positive) exists in num array.
        if closest < 0 and abs(closest) in nums:
            return abs(closest)                     # then return "positive" closest
        else:
            return closest              # if no duplicate, then simply return closest

        # Time: O(n) - only one loop.
        # Space: O(1) - no extra space is taken. 