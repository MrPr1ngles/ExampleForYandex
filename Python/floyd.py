from listSequence import ListSequence, Node
from option import Option

def detectCycle(sequence: ListSequence) -> bool:
    slow = fast = sequence.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def findCycleStart(sequence: ListSequence) -> Option:
    slow = fast = sequence.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            slow = sequence.head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return Option.some(slow.value)
    return Option.none()
