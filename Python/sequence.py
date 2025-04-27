from abc import ABC, abstractmethod

class Sequence(ABC):
    @abstractmethod
    def get(self, index):
        """Get element at index."""
        raise NotImplementedError

    @abstractmethod
    def getLength(self):
        """Get the length of the sequence."""
        raise NotImplementedError

    @abstractmethod
    def getFirst(self):
        """Get the first element of the sequence."""
        raise NotImplementedError

    @abstractmethod
    def getLast(self):
        """Get the last element of the sequence."""
        raise NotImplementedError

    @abstractmethod
    def getSubSequence(self, startIndex, endIndex):
        """
        Get subsequence from startIndex to endIndex (inclusive).
        """
        raise NotImplementedError

    @abstractmethod
    def append(self, item):
        """Append item to the end of the sequence."""
        raise NotImplementedError

    @abstractmethod
    def prepend(self, item):
        """Prepend item to the beginning of the sequence."""
        raise NotImplementedError

    @abstractmethod
    def insertAt(self, item, index):
        """Insert item at specified index."""
        raise NotImplementedError

    @abstractmethod
    def removeAt(self, index):
        """Remove item at specified index."""
        raise NotImplementedError
