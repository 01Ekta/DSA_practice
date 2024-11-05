from collections import Counter

class Solution:
    def findLHS(self, nums):
        count = Counter(nums)  # Get frequency of each element
        max_length = 0

        for num in count:
            if num + 1 in count:  # Check if there's an adjacent number
                # Calculate the length of harmonious subsequence
                max_length = max(max_length, count[num] + count[num + 1])

        return max_length