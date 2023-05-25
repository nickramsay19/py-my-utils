from nick.testing import limit_calls

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