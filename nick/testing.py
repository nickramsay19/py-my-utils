from __future__ import annotations
from typing import Callable
import functools
from meta import WrappedObject

_INCREMENT_ARG_TRANSFORM = lambda x: x + 1

def limit_calls(max_calls: int = 1, then = lambda *args, **kwargs: None):
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