class Calculator:
    """
    A simple calculator that works with strings.
    """

    def add(self, numbers: str) -> int:
        """
        Calculates the sum of numbers in a string.

        The numbers can be separated by default delimiters (comma or newline)
        or by a custom delimiter. When a custom delimiter is used, newlines
        are also treated as delimiters.
        Format for custom delimiter: "//[delimiter]\\n[numbers...]"

        Args:
            numbers: A string of numbers.

        Returns:
            The sum of the numbers.
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
        return sum(int(num) for num in parts)
