class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance_count = 0  # Counter for balance between 'L' and 'R'
        max_balanced_substrings = 0  # Maximum number of balanced substrings found

        for char in s:
        # Update balance_count based on the character
            if char == 'L':
                balance_count += 1
            elif char == 'R':
                balance_count -= 1

        # If balance_count is zero, we've found a balanced substring
            if balance_count == 0:
                max_balanced_substrings += 1

        return max_balanced_substrings