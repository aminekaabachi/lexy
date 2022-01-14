class Term():

    def __init__(self, name: str, definition: str = None, **metadata):
        self.name = name
        self.definition = definition
        self.metadata = metadata
        self.traces = []
        if type(name) != str:
            raise Exception("The term is not a string.")

    def __enter__(self):
        return self

    def __exit__(self, ext_typ, exc_value, traceback):
        pass  # do stuff

    def __str__(self):
        return self.name

    def __eq__(self, lvalue):
        return lvalue == self.name

    def __repr__(self):
        return repr(str(self.name))

    def __hash__(self):
        return hash(repr(self))

    def metadata(self):
        return self.metadata

    def definition(self):
        return self.definition

    def add_trace(self, trace):
        self.traces.append(trace)

    def describe(self):
        return {"name": self.name, "definition": self.definition, "usage_count": len(self.traces), "metadata": self.metadata}
