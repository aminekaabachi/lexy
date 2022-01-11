class Term():
      def __init__(self, name:str, comment:str=None, **metadata):
              self.name = name
              self.comment = comment
              self.metadata = metadata
              if type(name) != str:
                raise Exception("The term is not a string.")

      def __str__(self):
              return str(self.name)
      def __repr__(self):
              return str(self.name).__repr__()

      def metadata(self):
        return self.metadata
      
      def comment(self):
        return self.comment
      
      def describe(self):
        return {"name": self.name, "comment": self.comment, "metadata": self.metadata}