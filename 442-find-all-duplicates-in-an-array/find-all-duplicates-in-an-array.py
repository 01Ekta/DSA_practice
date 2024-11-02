class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        frequency = {}  # Dictionary to store the frequency of each integer
        result = []     # List to store the integers that appear twice

        # Count the frequency of each number in nums
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Check the frequency of each number and add duplicates to the result
        for num, count in frequency.items():
            if count == 2:
                result.append(num)

        return result
