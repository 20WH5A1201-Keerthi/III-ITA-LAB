class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
       
        maxSumBefore = nums[0]
        maxSumTotal = maxSumBefore
       
        for i in range(1, len(nums)):
            bestSumIsEitherThis = maxSumBefore + nums[i]
            orThis = nums[i]
           
            maxSumBefore = max(bestSumIsEitherThis, orThis)
            maxSumTotal = max(maxSumBefore, maxSumTotal)
           
        return maxSumTotal
