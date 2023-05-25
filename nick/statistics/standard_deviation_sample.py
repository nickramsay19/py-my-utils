def standard_deviation_sample(data: list) -> float:
    """
    Returns the standard deviation of data from a sample.
    :type data: list of int
    """

    # Check that the parameters are the correct type and value
    if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
    elif len(data) > 0:
        if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

    return (lambda d : (sum([(n - sum(d)/len(d))**2 for n in d])/(len(d)-1))**(1/2))(data)
