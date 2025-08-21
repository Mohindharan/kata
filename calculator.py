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

        if numbers.startswith("//"):
            # Custom delimiter logic
            delimiter_line, numbers_string = numbers.split('\n', 1)
            delimiter = delimiter_line[2]
            numbers_with_common_delimiter = numbers_string.replace('\n', delimiter)
            parts = numbers_with_common_delimiter.split(delimiter)
        else:
            # Default delimiter logic (comma and newline)
            numbers_with_common_delimiter = numbers.replace('\n', ',')
            parts = numbers_with_common_delimiter.split(',')

        # Convert to integers, filtering out empty strings that might result from splitting
        nums = [int(p) for p in parts if p]

     
        negatives = [n for n in nums if n < 0]

        # If negatives are found, raise an exception 
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        # Otherwise, return the sum of the numbers
        return sum(nums)
