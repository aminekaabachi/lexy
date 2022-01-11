from glossy.glossary import Glossary

def test_should_contain_term():
    g = Glossary()
    g("Hello")
    assert "Hello" in g.describe().keys()
