class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums) - 2):

            # Skip duplicate fixed values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                curr = nums[i] + nums[j] + nums[k]

                if curr < 0:
                    j += 1
                elif curr > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    # Move both pointers once
                    j += 1
                    k -= 1

                    # Skip duplicate j values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans