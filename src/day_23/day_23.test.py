import unittest

from src.day_23.day_23 import *


class TestDay23(unittest.TestCase):
    def test_next_destination_cup(self):
        self.assertEqual(next_destination_cup(3, 5), 2)
        self.assertEqual(next_destination_cup(2, 5), 1)
        self.assertEqual(next_destination_cup(1, 5), 5)

    def test_find_destination_cup(self):
        self.assertEqual(find_destination_cup(2, [8, 9, 3], 9), 1)
        self.assertEqual(find_destination_cup(2, [8, 9, 1], 9), 7)
        self.assertEqual(find_destination_cup(2, [8, 9, 1], 10), 10)

    def test_part_a(self):
        self.assertEqual(part_a('389125467'), '67384529')
        self.assertEqual(part_a('318946572'), '52864379')

    def test_pad_cups(self):
        starting_cups = [3, 4, 5, 2, 1]
        self.assertEqual(pad_cups(starting_cups, 5), starting_cups)
        self.assertEqual(pad_cups(starting_cups, 7), [3, 4, 5, 2, 1, 6, 7])

    def test_linked_list_to_string(self):
        linked_list = CircularLinkedList([2, 4, 5, 3, 1])
        self.assertEqual(linked_list.to_string(2), '2,4,5,3,1')
        self.assertEqual(linked_list.to_string(4), '4,5,3,1,2')
        self.assertEqual(linked_list.to_string(5), '5,3,1,2,4')
        self.assertEqual(linked_list.to_string(3), '3,1,2,4,5')
        self.assertEqual(linked_list.to_string(1), '1,2,4,5,3')

    def test_linked_list_get_node_with_value(self):
        linked_list = CircularLinkedList([2, 4, 5, 3, 1])
        resulting_node = linked_list.get_node_with_value(5)
        self.assertEqual(resulting_node.value, 5)
        self.assertEqual(resulting_node.next.value, 3)

    def test_linked_list_insert_after_value(self):
        linked_list = CircularLinkedList([2, 4, 5, 3, 1])
        five_node = linked_list.get_node_with_value(5)
        linked_list.insert_after(five_node, 6)
        six_node = linked_list.get_node_with_value(6)
        self.assertEqual(linked_list.to_string(2), '2,4,5,6,3,1')
        self.assertEqual(six_node, five_node.next)
        self.assertEqual(linked_list.get_node_with_value(3), six_node.next)

    def test_linked_list_remove_after_value(self):
        linked_list = CircularLinkedList([2, 4, 5, 3, 1])
        five_node = linked_list.get_node_with_value(5)
        result = linked_list.remove_after(five_node)
        self.assertEqual(result, 3)
        self.assertEqual(linked_list.to_string(2), '2,4,5,1')

    def test_prepare_linked_list(self):
        result = prepare_linked_list('34521', 10)
        self.assertEqual(result.to_string(3), '3,4,5,2,1,6,7,8,9,10')


if __name__ == '__main__':
    unittest.main()
