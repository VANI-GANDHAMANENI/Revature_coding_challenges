from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        return sum(v * (v - 1) // 2 for v in count.values())
solution = Solution()
nums = [1, 2, 3, 1, 1, 3]
print(solution.numIdenticalPairs(nums))