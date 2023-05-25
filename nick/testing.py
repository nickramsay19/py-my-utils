from __future__ import annotations
from typing import Any, Callable
import functools
from .meta import WrappedObject

_INCREMENT_ARG_TRANSFORM = lambda x: x + 1

def limit_calls(max_calls: int = 1, then = lambda *args, **kwargs: None) -> Callable:
    """A function decorator that limits the total number of calls executed of a function. Useful for ensuring that test cases are ran only once."""
    def decorator(func):
    
        # count function calls, value must be wrapped so it can be modified
        calls = WrappedObject(0) 
        get_calls = calls.GetGetter()
        inc_calls = calls.GetModifier(_INCREMENT_ARG_TRANSFORM)
        
        @functools.wraps(func)
        def wrapper(get_calls_get, inc_calls, *args, **kwargs):
            if get_calls() < max_calls:
                inc_calls()
                return func(*args, **kwargs)
            else:
                return then(*args, **kwargs)
        return lambda *args, **kwargs: wrapper(get_calls, inc_calls, *args, **kwargs)
    return decorator

def assert_error(exp_error: BaseException|type, func: Callable, *args, **kwargs) -> Any:
    """Debug assert that a call with provided args will result in the specified exception raised. Will raise an AssertionError. If exp_error is None, then assert that no error will be raised. For convinience, a successful call's value will be retured."""
    try: # call the given function, 
        return func(*args, **kwargs) # return its value in case the caller wants to do further checks
    except BaseException as e:
        if type(e) == exp_error or type(e) == type(exp_error): # caller expected this error, all is good
            return
        elif exp_error == None: # caller didn't except any error, hence None
            raise AssertionError(f"Function {func.__name__} raised {repr(e)}, but no error was expected.") from e
        else: # the caller didn't expect this error to be raised
            raise AssertionError(f"Function {func.__name__} raised {repr(e)}, but a {exp_error.__name__} was expected.") from e