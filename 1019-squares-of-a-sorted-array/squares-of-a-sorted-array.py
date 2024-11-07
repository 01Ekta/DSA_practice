class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # create a new array
        square = []
        
        for num in nums:  # iterate over elements of array
            square.append(num*num)  # square each element and add it into new array

        square.sort()  # we will sort the array after squaring the elements
        return square