from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Square each element
        square = [x * x for x in nums]
        
        # Sort the squared elements
        square.sort()
        
        # Return the sorted list of squares
        return square