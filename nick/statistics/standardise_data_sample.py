def standardise_data_sample(data: list) -> list:
    """
    Converts each value of a set of sample values to their coressponding z-scores.
    :type data: list of int
    """

    # Check that the parameters are the correct type and value
    if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
    elif len(data) > 0:
        if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

    return (lambda d : [(n - cls.mean(d))/cls.standard_deviation_sample(d) for n in d])(data)
