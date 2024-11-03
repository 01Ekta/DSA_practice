class Solution:
    def solveEquation(self, equation: str) -> str:
        # Split the equation at '=' to get the left and right sides
        left, right = equation.split('=')
        
        # Helper function to process each side and get the x coefficient and constant
        def parse_side(side):
            x_coeff = 0  # Coefficient of x
            constant = 0  # Constant value
            num = ''  # Temporary number storage
            sign = 1  # 1 for positive, -1 for negative
            for char in side + '+':  # Add a final '+' to handle the last term
                if char.isdigit():
                    num += char
                elif char == 'x':
                    if num == '':  # Case like 'x' or '-x'
                        x_coeff += sign
                    else:
                        x_coeff += sign * int(num)
                    num = ''
                elif char in '+-':
                    if num:
                        constant += sign * int(num)
                        num = ''
                    sign = 1 if char == '+' else -1
            return x_coeff, constant
        
        # Get the x coefficient and constant for both sides
        left_x, left_const = parse_side(left)
        right_x, right_const = parse_side(right)
        
        # Combine terms
        total_x = left_x - right_x
        total_const = right_const - left_const
        
        # Analyze the solution
        if total_x == 0:
            if total_const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={total_const // total_x}"        