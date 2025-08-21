class Calculator:
    """
    A simple calculator that works with strings.
    """

    def add(self, numbers: str) -> int:

        if not numbers:
            return 0
        
        numbers_with_common_delimiter = numbers.replace('\n', ',')
        parts = numbers_with_common_delimiter.split(',')
        return sum(int(num) for num in parts)

