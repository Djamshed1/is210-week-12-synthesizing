#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 12 Synthesizing task 01"""

class BaseError(Exception):
    """A BaseError exception class name"""
    pass

class StringError(BaseError, TypeError):
    """A StringError exception class name"""
    pass

class NumberError(BaseError, TypeError):
    """A NumberError exception class name"""
    pass

class NonZeroError(NumberError):
    """A NonZeroError exception class name"""
    pass
