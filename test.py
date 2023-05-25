from nick import *
from nick.testing import *
from nick.func import *

def test_limit_calls():
    f1 = limit_calls(1)(lambda: 1)
    assert f1() == 1
    assert f1() == None
    assert f1() == None
    
    f2 = limit_calls(2, lambda *args, **kwargs: args[1])(lambda *args, **kwargs: args[0])
    assert f2(0,1) == 0
    assert f2(0,1) == 0
    assert f2(0,1) == 1
    assert f2(0,1) == 1

def test_OneIndexedListt():
    l = OneIndexedList([1,2,3])
    assert l[1] == 1
    assert l[2] == 2
    assert l[3] == 3
    assert sum(l) == 6
    assert len(l) == 3
    
    l[2] = 100
    assert l[1] == 1
    assert l[2] == 100
    assert l[3] == 3

def test_max_idx():
    assert max_idx([1,2,3]) == (2, 3), f"{max_idx([1,2,3])} != (2,3)"
    assert max_idx([3,2,1]) == (0, 3)
    assert max_idx([98, 101, 21, 42, 101, 26, 974, 57, 421]) == (6, 974)

def test_take_args_as_list():
    # simple case, no positionals
    @take_args_as_list() # NOTE: must use empty parenthesis
    def f1(L: list[any]):
        return L[0]
    
    assert (r := f1(3,2,1)) == 3, r
    assert (r := f1([3,2,1])) == 3, r
    
    # with positionals
    @take_args_as_list(1)
    def f2(n: int, L: list[any]):
        return n + L[0]
    
    assert (r := f2(10, 3,2,1)) == 13, r
    assert (r := f2(10, [3,2,1])) == 13, r

def test_validate_args():
    ALL_INT_ARG_VALIDATOR: Callable = lambda *args, **kwargs: None if (r:=all(t:=[isinstance(a, int) for a in args])) else TypeError("All provided arguments must be integers.")
    test_func: Callable = validate_args(ALL_INT_ARG_VALIDATOR)(lambda *args, **kwargs: 0 if len(args) < 1 else sum(args))

    assert_error(None, test_func, 1,2,3)
    assert_error(None, test_func)
    assert_error(None, test_func, -64)
    assert_error(TypeError, test_func, 'str')
    assert_error(TypeError, test_func, 1.5)
    assert_error(TypeError, test_func, 1,2,3,4,'5')

def main():
    test_limit_calls()
    test_OneIndexedListt()
    test_max_idx()
    test_take_args_as_list_decorator_factory()
    test_validate_args()

if __name__ == '__main__':
    main()