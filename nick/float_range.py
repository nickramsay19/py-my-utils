def float_range(precision: int, min: int or float = 0, max: int or float = 1, inclusive: bool = False) -> list:
    """Returns a list of floats of certain precision within a defined range."""

    # Check that the parameters are the correct type and value.
    if type(precision) != int: raise TypeError('\'precision\' must be of type int.')
    elif precision < 1 or precision > 8: raise ValueError('\'precision\' must be between 1 and 8.')
    elif type(min) != int and type(min) != float: raise TypeError('\'min\' must be of type int or float.')
    elif type(max) != int and type(max) != float: raise TypeError('\'max\' must be of type int or float.')
    elif type(inclusive) != bool: raise TypeError('\'inclusive\' must be of type bool.')

    # Return the result of a list comprehension.
    return [float(x) / 10**precision for x in range(int(min * (10**precision)), int(max * (10**precision) + int(inclusive)))]
