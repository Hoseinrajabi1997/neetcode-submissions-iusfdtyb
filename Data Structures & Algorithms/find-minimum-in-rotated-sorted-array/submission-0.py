class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            # If the current range is already sorted, the leftmost is the minimum
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            # 🔹 Key change:
            # If mid > right, that means the min is to the right of mid
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        return res
