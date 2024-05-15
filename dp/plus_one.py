def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
    
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        # If all digits were 9, create a new array with one more digit
        return [1] + [0] * n
        
