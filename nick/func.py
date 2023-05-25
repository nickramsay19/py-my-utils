from __future__ import annotations
from typing import Any, Callable
import functools

def transform_args(arg_transform: Callable[[list, dict], tuple[list, dict]]) -> Callable:
    """Decorator factory for functions to apply an arg transform on each call."""
    def _decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def _wrapper(*args, **kwargs) -> any:
            t_args, t_kwargs = arg_transform(*args, **kwargs)
            return func(*t_args, **t_kwargs)
        return _wrapper
    return _decorator

def take_args_as_list(pos: int = 0): # the factory
    def take_args_as_list_decorator(func): # the actual decorator 
        @functools.wraps(func) # ensures decorator wrapping preserves original name
        def wrapper(*args, **kwargs):
            # extract only the desired list args
            normal_args = args[:pos]
            list_args = args[pos:]
            
            L: List[any] = list(list_args) # convert args tuple to list
            
            # check if we were passed a regular list
            if len(list_args) == 1 and type(list_args[0]) == list:
                # revert L back into the passed list
                L = list_args[0]
            
            return func(*normal_args, L, **kwargs)
        return wrapper
    return take_args_as_list_decorator

def validate_args(arg_validator: Callable) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # an arg_validator can raise an error by itself, or return a BaseException for us to throw for it 
            validation = arg_validator(*args, **kwargs)
            if validation != None:
                raise validation from validation

            return func(*args, **kwargs)
        return wrapper
    return decorator