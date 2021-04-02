"""
##############################################################################
#
#   Custom Exceptions
#
#   AUTHOR: Maciej_Bak
#   AFFILIATION: University_of_Basel
#   AFFILIATION: Swiss_Institute_of_Bioinformatics
#   CONTACT: wsciekly.maciek@gmail.com
#   CREATED: 01-04-2021
#   LICENSE: MIT
#
##############################################################################
"""


class Error(Exception):
    """Base class for other exceptions.

    Args:
        Exception (Exception): built-in Exception class
    """

    pass


class IncorrectValueError(Error):
    """Handling incorrect values of user's arguments.

    Args:
        Error (Error): Base class for other exceptions.
    """

    def __init__(
        self,
        parameter,
        message="Please check the documentation for expected argument values.",
    ):
        """Class initializer.

        Args:
            parameter (str): parameter name
            message (str, optional): error message.
                Defaults to "Please check the documentation
                for expected argument values.".
        """
        self.parameter = parameter
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        """Display the error message.

        Returns:
            str: error message
        """
        return f"Incorrect value for {self.parameter}. {self.message}"
