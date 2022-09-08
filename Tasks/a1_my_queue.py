"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.queue = []  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.queue.append(elem)
        print(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        temp = self.queue[0]
        del self.queue[0]

        return temp

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if not self.queue:
            return None
        if ind > len(self.queue)-1:
            return None

        print(ind)
        return self.queue[ind]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """


        self.queue.clear()
        return None
