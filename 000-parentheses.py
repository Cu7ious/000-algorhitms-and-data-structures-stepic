#! /usr/bin/env python3
import sys


class Stack:
    def __init__(self):
        self.stack = []

    def print(self, s=""):
        print(s, self.stack)

    def push(self, key):
        self.stack.append(key)

    def top(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) is 0


def parenth_parser(string=""):
    stack = Stack()
    symbols = {"{": "}", "(": ")", "[": "]"}
    idx = -1

    if len(string) is 1:
        return 1

    for c in string:
        idx += 1

        if c in symbols.keys():
            stack.push([c, string.index(c, idx)])
        elif c not in symbols.values():
            continue
        else:
            if stack.is_empty():
                # stack.print("stack is empty")
                return idx + 1

            top = stack.pop()[0]
            if c not in symbols.values() or symbols[top] != c:
                # stack.print("symbols[top] != c")
                return (idx + 1)

    if stack.is_empty() is False:
        # stack.print("stack.is_empty() is False")
        return stack.pop()[1] + 1

    return "Success"

if __name__ == "__main__":
    # s = sys.stdin.read()
    s = sys.argv[1]
    print(parenth_parser(s))
