class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Square each element
        square = []
        
        for num in nums:
            square.append(num*num)

        square.sort()
        return square