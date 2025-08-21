import re

class Calculator:
    """
    A simple calculator that works with strings.
    """

    def add(self, numbers: str) -> int:
        """
        Calculates the sum of numbers in a string.
        
        Args:
            numbers: A string of numbers.

        Returns:
            The sum of the numbers.

        Raises:
            ValueError: If the input string contains negative numbers.
        """

        if not numbers:
            return 0

        delimiters = [","]
        numbers_string = numbers
        if numbers.startswith("//"):
            # Custom delimiter logic
            delimiter_line, numbers_string = numbers.split('\n', 1)
            # Find all delimiters in brackets: e.g., //[*][%]\n
            found_delimiters = re.findall(r'\[(.*?)\]', delimiter_line)
            if found_delimiters:
                delimiters = found_delimiters
            else:
                # Fallback for single char delimiter: e.g., //;\n
                delimiters = [delimiter_line[2]]

        # Create a regex pattern from all delimiters (custom + newline) and split the string
        pattern = '|'.join(map(re.escape, delimiters + ['\n']))
        parts = re.split(pattern, numbers_string)

        # Convert to integers, filtering out empty strings that might result from splitting
        nums = [int(p) for p in parts if p]

        negatives = [n for n in nums if n < 0]

        # If negatives are found, raise an exception
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        # Otherwise, return the sum of the numbers
        return sum(nums)
