class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for digits in str(n):
            digits = int(digits)
            product *= digits
            sum += digits
        return product - sum
