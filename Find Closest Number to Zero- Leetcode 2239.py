class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]

        for i in range(1,len(nums)): 
            if abs(nums[i]) < abs(min): 
                min  = nums[i]
            elif abs(nums[i]) == abs(min):
                min = max(min, nums[i])
        return min 
