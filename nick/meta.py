from __future__ import annotations
from typing import Callable

class WrappedObject:
    """Wrap atomics and sentinals into a pseudo pass by reference object."""
    def __init__(self, val: any):
        self._val: List[any] = [val]

    def _get(self) -> any:
        return self._val[0]
    
    def _set(self, val: any) -> None:
        self._val = [val]

    def GetGetter(self) -> Callable[[], any]:
        return lambda: self._get()
        
    def GetSetter(self) -> Callable[[any], None]:
        return lambda val: self._set(val)
    
    def GetModifier(self, transform: Callable[[any], any]) -> Callable[[any], None]:
        return lambda: self._set(transform(self._val[0]))
    
    def GetValue(self) -> any:
        v = self._get()
        return v