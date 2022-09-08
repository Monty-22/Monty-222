"""
My little Stack
"""
from typing import Any


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.stack.append(elem)

        print(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """
        if not self.stack:
            return None
        tmp = self.stack[len(self.stack) - 1]
        self.stack.pop()
        return tmp

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place
        """
        temp = self.stack[-ind-1]

        print(ind)
        return temp

    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.stack.clear()
        return None
