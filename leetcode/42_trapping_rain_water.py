"""Created by sgoswami on 8/11/17."""
"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much 
water it is able to trap after raining."""
import sys


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left_max, right_max = [0 for _ in range(len(height))], [0 for _ in range(len(height))]
        left_max[0], right_max[-1] = height[0], height[-1]
        curr_left = curr_right = -sys.maxsize

        for i in range(1, len(height)):
            left_max[i] = curr_left = max(curr_left, height[i])
            right_max[-i-1] = curr_right = max(curr_right, height[-i-1])

        total = 0
        for i in range(len(height)):
            total += max((min(left_max[i], right_max[i]) - height[i]), 0)

        return total


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))




