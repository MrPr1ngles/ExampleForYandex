# arraySequence.py
from sequence import Sequence
from error import IndexOutOfBoundsError

class ArraySequence(Sequence):
    def __init__(self, data=None):
        if data is None:
            self._data = []
        else:
            self._data = list(data)

    def get(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexOutOfBoundsError()
        return self._data[index]

    def getLength(self):
        return len(self._data)

    def getFirst(self):
        if not self._data:
            raise IndexOutOfBoundsError("Sequence is empty")
        return self._data[0]

    def getLast(self):
        if not self._data:
            raise IndexOutOfBoundsError("Sequence is empty")
        return self._data[-1]

    def getSubSequence(self, startIndex, endIndex):
        if (startIndex < 0 or endIndex < 0 or
            startIndex >= len(self._data) or endIndex >= len(self._data) or
            startIndex > endIndex):
            raise IndexOutOfBoundsError()
        sub_data = self._data[startIndex:endIndex+1]
        return ArraySequence(sub_data)

    def append(self, item):
        self._data.append(item)

    def prepend(self, item):
        self._data.insert(0, item)

    def insertAt(self, item, index):
        if index < 0 or index > len(self._data):
            raise IndexOutOfBoundsError()
        self._data.insert(index, item)

    def removeAt(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexOutOfBoundsError()
        self._data.pop(index)

    def __str__(self):
        return f"{self.__class__.__name__}({self._data})"

class ImmutableArraySequence(ArraySequence):
    def __init__(self, data=None):
        super().__init__(data)

    def getSubSequence(self, startIndex, endIndex):
        if (startIndex < 0 or endIndex < 0 or
            startIndex >= len(self._data) or endIndex >= len(self._data) or
            startIndex > endIndex):
            raise IndexOutOfBoundsError()
        sub_data = self._data[startIndex:endIndex+1]
        return ImmutableArraySequence(sub_data)

    def append(self, item):
        new_data = list(self._data)
        new_data.append(item)
        return ImmutableArraySequence(new_data)

    def prepend(self, item):
        new_data = list(self._data)
        new_data.insert(0, item)
        return ImmutableArraySequence(new_data)

    def insertAt(self, item, index):
        if index < 0 or index > len(self._data):
            raise IndexOutOfBoundsError()
        new_data = list(self._data)
        new_data.insert(index, item)
        return ImmutableArraySequence(new_data)

    def removeAt(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexOutOfBoundsError()
        new_data = list(self._data)
        new_data.pop(index)
        return ImmutableArraySequence(new_data)
