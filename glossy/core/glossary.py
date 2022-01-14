from glossy.core.term import Term
import traceback
import inspect

class Glossary():
    def __init__(self, terms={}, relations={}):
      self.terms = terms
      self.relations = relations

    def update(self, name, comment=None, relations=[], **metadata):
      t = Term(name, comment, **metadata)
      self.terms[name] = t
      self.relations[name] = relations
      return t
    
    def find(self, name: str):
      if name in self.terms.keys():
        return self.terms[name]
      return None
    
    def describe(self):
      d = {}
      for term in self.terms:
        d[self.terms[term].name] = dict(self.terms[self.terms[term].name].describe(), **{"relations": self.relations[self.terms[term].name]})
      return d

    def relations_graph(self):
      r = {}
      for term in self.terms:
        r[self.terms[term].name] = self.relations[self.terms[term].name]
      return r

    def __call__(self, name, comment=None, force_update=False, **metadata):
        term = self.find(name) 
        if term != None and not force_update:
          term.add_trace(inspect.stack()[1])
          return str(term)
        return self.update(name, comment, **metadata)
        