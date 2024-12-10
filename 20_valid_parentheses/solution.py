from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        if len(s) % 2 == 1:
            return False
        for letter in s:
            if letter in ('(', '[', '{'):
                stack.add(letter)
            else:
                compare_object = stack.pop()
                if (
                        (letter == '}' and compare_object != '{') or
                        (letter == ']' and compare_object != '[') or
                        (letter == ')' and compare_object != '(')
                ):
                    return False
        return True

class Stack:
    def __init__(self):
        self.queue: List[str] = list()

    def add(self, element: str) -> None:
        self.queue.append(element)

    def pop(self) -> str:
        return self.queue.pop()

if __name__ == '__main__':
    test_cases = [
        ('({[[]]})', True),
        ('(', False),
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('((', False),
        ('))', False)
    ]
    sol = Solution()
    for test_case, expected_result in test_cases:
        actual_result = sol.isValid(test_case)
        print(
            f'{test_case = } | {expected_result = } | {actual_result = }, '
            f'results match = {expected_result == actual_result}'
        )