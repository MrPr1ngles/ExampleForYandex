from sequence import Sequence
from error import IndexOutOfBoundsError

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"Node({self.value})"

class ListSequence(Sequence):
    def __init__(self, data=None):
        self.head = None
        self._length = 0
        if data is not None:
            for item in data:
                self.append(item)

    def getLength(self):
        return self._length

    def get(self, index):
        if index < 0 or index >= self._length:
            raise IndexOutOfBoundsError()
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def getFirst(self):
        if not self.head:
            raise IndexOutOfBoundsError("Sequence is empty")
        return self.head.value

    def getLast(self):
        if not self.head:
            raise IndexOutOfBoundsError("Sequence is empty")
        current = self.head
        while current.next:
            current = current.next
        return current.value

    def getSubSequence(self, startIndex, endIndex):
        if (startIndex < 0 or endIndex < 0 or
            startIndex >= self._length or endIndex >= self._length or
            startIndex > endIndex):
            raise IndexOutOfBoundsError()
        sub_list = []
        current = self.head
        for i in range(endIndex+1):
            if i >= startIndex:
                sub_list.append(current.value)
            current = current.next
        return ListSequence(sub_list)

    def append(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._length += 1

    def prepend(self, item):
        new_node = Node(item, self.head)
        self.head = new_node
        self._length += 1

    def insertAt(self, item, index):
        if index < 0 or index > self._length:
            raise IndexOutOfBoundsError()
        if index == 0:
            self.prepend(item)
            return
        new_node = Node(item)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self._length += 1

    def removeAt(self, index):
        if index < 0 or index >= self._length:
            raise IndexOutOfBoundsError()
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self._length -= 1

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return f"{self.__class__.__name__}({values})"

class ImmutableListSequence(ListSequence):
    def __init__(self, data=None):
        self.head = None
        self._length = 0
        if data is not None:
            for item in data:
                ListSequence.append(self, item)

    def append(self, item):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        values.append(item)
        return ImmutableListSequence(values)

    def prepend(self, item):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        values.insert(0, item)
        return ImmutableListSequence(values)

    def insertAt(self, item, index):
        if index < 0 or index > self._length:
            raise IndexOutOfBoundsError()
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        values.insert(index, item)
        return ImmutableListSequence(values)

    def removeAt(self, index):
        if index < 0 or index >= self._length:
            raise IndexOutOfBoundsError()
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        values.pop(index)
        return ImmutableListSequence(values)

    def getSubSequence(self, startIndex, endIndex):
        if (startIndex < 0 or endIndex < 0 or
            startIndex >= self._length or endIndex >= self._length or
            startIndex > endIndex):
            raise IndexOutOfBoundsError()
        values = []
        current = self.head
        for i in range(endIndex+1):
            if i >= startIndex:
                values.append(current.value)
            current = current.next
        return ImmutableListSequence(values)

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return f"{self.__class__.__name__}({values})"
