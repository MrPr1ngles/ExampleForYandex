import unittest
import sys
sys.path.append('.')  

from arraySequence import ArraySequence, ImmutableArraySequence
from listSequence import ListSequence, ImmutableListSequence, Node
from option import Option
from error import IndexOutOfBoundsError, InvalidInputError
from floyd import detectCycle, findCycleStart

class TestArraySequence(unittest.TestCase):
    def test_append_prepend(self):
        seq = ArraySequence([1, 2, 3])
        self.assertEqual(str(seq), 'ArraySequence([1, 2, 3])')
        seq.append(4)
        self.assertEqual(seq.getLast(), 4)
        seq.prepend(0)
        self.assertEqual(seq.getFirst(), 0)
        self.assertEqual(seq.getLength(), 5)

    def test_get_and_remove(self):
        seq = ArraySequence([10, 20, 30])
        self.assertEqual(seq.get(1), 20)
        with self.assertRaises(IndexOutOfBoundsError):
            seq.get(5)
        seq.removeAt(1)
        self.assertEqual(seq.get(1), 30)
        with self.assertRaises(IndexOutOfBoundsError):
            seq.removeAt(10)

    def test_subsequence(self):
        seq = ArraySequence([1, 2, 3, 4, 5])
        sub = seq.getSubSequence(1, 3)
        self.assertIsInstance(sub, ArraySequence)
        self.assertEqual(str(sub), 'ArraySequence([2, 3, 4])')
        with self.assertRaises(IndexOutOfBoundsError):
            seq.getSubSequence(3, 1)

    def test_immutable_array(self):
        seq = ImmutableArraySequence([5, 6, 7])
        new_seq = seq.append(8)
        self.assertIsInstance(new_seq, ImmutableArraySequence)
        self.assertEqual(str(new_seq), 'ImmutableArraySequence([5, 6, 7, 8])')
        self.assertEqual(str(seq), 'ImmutableArraySequence([5, 6, 7])')
        seq2 = seq.removeAt(1)
        self.assertEqual(str(seq2), 'ImmutableArraySequence([5, 7])')
        self.assertEqual(str(seq), 'ImmutableArraySequence([5, 6, 7])')

class TestListSequence(unittest.TestCase):
    def test_append_prepend(self):
        seq = ListSequence([10, 20])
        self.assertEqual(str(seq), 'ListSequence([10, 20])')
        seq.append(30)
        self.assertEqual(seq.getLast(), 30)
        seq.prepend(5)
        self.assertEqual(seq.getFirst(), 5)

    def test_get_and_remove(self):
        seq = ListSequence([100, 200, 300])
        self.assertEqual(seq.get(2), 300)
        with self.assertRaises(IndexOutOfBoundsError):
            seq.get(4)
        seq.removeAt(0)
        self.assertEqual(seq.getFirst(), 200)
        with self.assertRaises(IndexOutOfBoundsError):
            seq.removeAt(5)

    def test_subsequence(self):
        seq = ListSequence([1, 2, 3, 4, 5])
        sub = seq.getSubSequence(2, 4)
        self.assertIsInstance(sub, ListSequence)
        self.assertEqual(str(sub), 'ListSequence([3, 4, 5])')
        with self.assertRaises(IndexOutOfBoundsError):
            seq.getSubSequence(-1, 2)

    def test_immutable_list(self):
        seq = ImmutableListSequence([7, 8, 9])
        new_seq = seq.append(10)
        self.assertIsInstance(new_seq, ImmutableListSequence)
        self.assertEqual(str(new_seq), 'ImmutableListSequence([7, 8, 9, 10])')
        self.assertEqual(str(seq), 'ImmutableListSequence([7, 8, 9])')
        seq2 = seq.insertAt(6, 0)
        self.assertEqual(str(seq2), 'ImmutableListSequence([6, 7, 8, 9])')

class TestOption(unittest.TestCase):
    def test_option_some_none(self):
        some = Option.some(10)
        self.assertTrue(some.isSome())
        self.assertFalse(some.isEmpty())
        self.assertEqual(some.get(), 10)
        self.assertEqual(some.getOrElse(0), 10)
        none = Option.none()
        self.assertTrue(none.isEmpty())
        self.assertFalse(none.isSome())
        self.assertEqual(none.getOrElse(5), 5)
        with self.assertRaises(ValueError):
            none.get()
        self.assertEqual(repr(none), 'Option.none')
        self.assertEqual(repr(some), 'Option(10)')

class TestErrors(unittest.TestCase):
    def test_exceptions(self):
        with self.assertRaises(IndexOutOfBoundsError):
            raise IndexOutOfBoundsError('Test')
        with self.assertRaises(InvalidInputError):
            raise InvalidInputError('Test')

class TestFloyd(unittest.TestCase):
    def setUp(self):
        def build_sequence(values):
            seq = ListSequence(values)
            nodes = []
            current = seq.head
            while current:
                nodes.append(current)
                current = current.next
            return seq, nodes
        self.build_sequence = build_sequence

    def test_no_cycle(self):
        seq, _ = self.build_sequence([1, 2, 3, 4, 5])
        self.assertFalse(detectCycle(seq))
        self.assertTrue(findCycleStart(seq).isNone())

    def test_cycle_at_head(self):
        seq, nodes = self.build_sequence([10, 20, 30])
        nodes[-1].next = nodes[0]
        self.assertTrue(detectCycle(seq))
        start_opt = findCycleStart(seq)
        self.assertTrue(start_opt.isSome())
        self.assertEqual(start_opt.get(), 10)

    def test_cycle_in_middle(self):
        seq, nodes = self.build_sequence([5, 6, 7, 8, 9])
        nodes[-1].next = nodes[2]
        self.assertTrue(detectCycle(seq))
        start_opt = findCycleStart(seq)
        self.assertTrue(start_opt.isSome())
        self.assertEqual(start_opt.get(), 7)

    def test_single_node_no_cycle(self):
        seq, nodes = self.build_sequence([42])
        self.assertFalse(detectCycle(seq))
        self.assertTrue(findCycleStart(seq).isNone())

    def test_single_node_cycle_to_self(self):
        seq, nodes = self.build_sequence([99])
        nodes[0].next = nodes[0]
        self.assertTrue(detectCycle(seq))
        start_opt = findCycleStart(seq)
        self.assertTrue(start_opt.isSome())
        self.assertEqual(start_opt.get(), 99)


if __name__ == '__main__':
    unittest.main()
