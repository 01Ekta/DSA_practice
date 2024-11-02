class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # we use two-pointer 
        i, j = 0, len(s) - 1
        while i < j:   # here if length of string is even, then character swapped easily
        # but string length is odd, then middle element will stay at position in string as well reversed string and other element would be swapped
            s[i], s[j] = s[j], s[i]     # swap pointer character
            i += 1                      # increment 1st pointer by 1
            j -= 1                      # decrement 1st pointer by 1 
