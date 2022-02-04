class Solution:
    def jump(self, nums: list[int]) -> int:
        n=len(nums)
        if n == 1:
            return 0
        if nums[0] >= n-1:
            return 1

        max_reach = 0
        steps = nums[0]
        jumps_needed = 0

        for i in range(1,n-1):
            max_reach = max(max_reach, i+nums[i])
            steps -= 1
            if steps == 0:
                steps = max_reach - i
                jumps_needed += 1

        return jumps_needed + 1