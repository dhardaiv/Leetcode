class Solution(object):
    def containsDuplicate(self, nums):
        map = {}

        for n in nums: 
            if n in map: 
                return True 
            map[n] = n
        return False
