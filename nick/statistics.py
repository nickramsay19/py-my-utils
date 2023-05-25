from __future__ import annotations
from typing import Callable

def mean(data: list) -> float:
    """
    Returns the standard deviation of a set of values
    :type data: list of int
    """

    # Check that the parameters are the correct type and value
    if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
    elif len(data) > 0:
        if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

    return (lambda d : sum(n for n in d)/len(d))(data)

def standard_deviation_population(data: list) -> float:
    """
    Returns the standard deviation of data from a population.
    :type data: list of int
    """

    # Check that the parameters are the correct type and value
    if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
    elif len(data) > 0:
        if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

    return (lambda d : (sum([(n - sum(d)/len(d))**2 for n in d])/(len(d)))**(1/2))(data)

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

def standardise_data_population(data: list) -> list:
    """
    Converts each value of a set of population values to their coressponding z-scores.
    :type data: list of int
    """

    # Check that the parameters are the correct type and value
    if type(data) != list: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')
    elif len(data) > 0:
        if not type(data[0]) == int and not type(data[0]) == float: raise TypeError('\'data\' must be of type \'list of int\' or \'list of float\'.')

    return (lambda d : [(n - cls.mean(d))/cls.standard_deviation_population(d) for n in d])(data)

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



