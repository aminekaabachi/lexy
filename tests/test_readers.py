import glossy as g
import os

def test_read_glossary_from_csv():
    filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'dummy.csv')
    dummy = g.from_csv(filepath)
    assert dummy("aaaa").metadata == {'hello': 'eeee', 'zoona': 'dfdf'}
    assert dummy("dfdfd").metadata == {'hello': 'dfddf', 'zoona': 'dfdfd'}

def test_read_glossary_with_no_metadata_from_csv():
    filepath = os.path.join(os.path.dirname(__file__), 'fixtures', 'dummy_nometadata.csv')
    dummy = g.from_csv(filepath)
    assert dummy("aaaa").definition == "dddd"
    assert dummy("aaaa").metadata == {}

