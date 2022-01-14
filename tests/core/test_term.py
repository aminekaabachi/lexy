import glossy as g

def test_should_repr_like_string():
    t = g.Term("hello")
    assert t.__repr__() == t.__repr__()

def test_should_str_like_string():
    t = g.Term("hello")
    assert t.__str__() == "hello".__str__()
    