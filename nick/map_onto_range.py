def map_onto_range(value: int or float, inMin: int or float, inMax: int or float, outMin: int or float, outMax: int or float) -> int or float:
    """Returns a mapped value to a new range."""

    # check that the parameters are the correct type and value.
    if type(value) != int and type(value) != float: raise TypeError('\'value\' must be of type int or float.')
    elif type(inMin) != int and type(inMin) != float: raise TypeError('\'inMin\' must be of type int or float.')
    elif type(inMax) != int and type(inMax) != float: raise TypeError('\'inMax\' must be of type int or float.')
    elif type(outMin) != int and type(outMin) != float: raise TypeError('\'outMin\' must be of type int or float.')
    elif type(outMax) != int and type(outMax) != float: raise TypeError('\'outMax\' must be of type int or float.')
    elif value < inMin or value > inMax: raise ValueError('\'value\' must be in the range of \'inMin\' and \'inMax\'.')


    # return and map the value
    return outMin + (float(value - inMin) / float(inMax - inMin) * outMax - outMin)
