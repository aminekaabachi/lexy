import lexy as g

def test_should_contain_term():
    _ = g.Glossary()
    _("Hello")
    assert "Hello" in _.describe().keys()
