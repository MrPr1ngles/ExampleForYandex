class Option:
    """
    Represents an optional value. Option(value) is Some(value) if value is not None,
    otherwise represents None.
    """
    def __init__(self, value):
        self._value = value

    @classmethod
    def some(cls, value):
        if value is None:
            raise ValueError("Cannot create Option.some with None value")
        return cls(value)

    @classmethod
    def none(cls):
        return cls(None)

    def isEmpty(self):
        return self._value is None

    def isSome(self):
        return self._value is not None

    def get(self):
        if self.isEmpty():
            raise ValueError("No value present")
        return self._value

    def getOrElse(self, default):
        return self._value if self._value is not None else default

    def __eq__(self, other):
        if not isinstance(other, Option):
            return False
        return self._value == other._value

    def __repr__(self):
        if self.isEmpty():
            return "Option.none"
        return f"Option({self._value})"
