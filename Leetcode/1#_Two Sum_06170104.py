class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for k in range(n,i+1,-1):
                if nums[i] + nums[k-1] == target:
                    return [i,k-1]
