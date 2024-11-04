class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total_sum = 0
        for i in range(1,n+1):  #n + 1 is used to ensure that the loop includes the number n itself. In Python, the range() function generates numbers up to (but not including) the end value, so range(1, n) would stop at n - 1.
            if i%3==0 or i%5 == 0 or i%7 == 0:
                total_sum += i
        return total_sum