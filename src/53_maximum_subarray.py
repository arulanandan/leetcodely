"""Created by sgoswami on 7/31/17."""
"""Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6."""
import sys

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum, max_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if curr_sum + nums[i] > 0:
                curr_sum += nums[i]
            else:
                curr_sum = 0
            max_sum = max(curr_sum, max_sum)
        return max_sum

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
