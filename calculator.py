class Calculator:
    """
    A simple calculator that works with strings.
    """

    def add(self, numbers: str) -> int:

        if not numbers:
            return 0

        parts = numbers.split(',')
        return sum(int(num) for num in parts)

