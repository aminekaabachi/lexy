class Term():
    def __init__(self, name: str, definition: str = None, **metadata):
        self.name = name
        self.definition = definition
        self.metadata = metadata
        if type(name) != str:
            raise Exception("The term is not a string.")

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return repr(str(self.name))

    def __hash__(self):
        return hash(repr(self))

    def metadata(self):
        return self.metadata

    def definition(self):
        return self.definition

    def describe(self):
        return {"name": self.name, "definition": self.definition, "metadata": self.metadata}
