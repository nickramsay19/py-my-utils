from __future__ import annotations
from typing import Any, Callable, Type

'''
    ArgTuple
    Specifies a standardisation for describing the type of the idiomatic (*args, **kwargs) tuple. 

    The tuple should always contain two elements, fields should be set to "None" when absent.
'''
ArgTuple = tuple[
    tuple[Type, ...] | None, 
    dict[str, Any] | None
]

'''
    ArgTupleTransform
    A function that takes an ArgTuple and maps it to another ArgTuple object. 

    For clarity, it is advised to use the explicit form "Callable[ArgTuple, ArgTuple]" instead of "ArgTupleTransform".
'''
ArgTupleTransform = Callable[ArgTuple, ArgTuple]

'''
    ArgTupleValidator
    A function that returns a boolean indication of a valid ArgTuple.
'''
ArgTupleValidator = Callable[ArgTuple, bool]