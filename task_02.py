#!/usr/bin/env python
# -*- conding: utf-8 -*-
"""Week 12 synthesizing task 02"""

class CustomError(Exception):
    """This is a custom exception class."""
    
    def __init__(self, msg, cause):
        """CustomError custructor.

        Args:
            message(str): A message that will show up.
            cause(str): A cause of exception error.

        Returns:
            cause(str): Returns the cause of an exception error.

        Examples:
            >>> myerr = CustomError('Whoah!', cause='Messed up!')
            >>> print myerr.cause
            Messed up! 
        """
        Exception.__init__(self, msg)
        self.cause = cause
