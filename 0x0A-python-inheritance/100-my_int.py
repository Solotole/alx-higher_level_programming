#!/usr/bin/python3
"""class int ovewritting"""


class MyInt(int):
    """Rebel class"""
    def __eq__(self, other):
        """custom __eq__ magic method

        Args:
            other (int): other value to be compared
            against

        Returns:
            return boolean value opposite to expected
        """
        result = super().__ne__(other)
        return result

    def __ne__(self, other):
        """custom __ne__ magic method

        Args:
            other (int): other value to be compared against

        Returns:
            return boolean value opposite to expected
        """
        result = super().__eq__(other)
        return result
