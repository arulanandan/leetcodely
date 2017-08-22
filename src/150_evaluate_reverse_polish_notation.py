"""Created by sgoswami on 8/9/17."""
"""Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression."""
import collections

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = collections.deque()
        for item in tokens:
            if item.isdigit():
                stack.append(int(item))
            elif item[1:].isdigit():
                stack.append(int(item))
            else:
                curr = stack.pop()
                prev = stack.pop()
                if item == '+':
                    total = prev + curr
                elif item == '-':
                    total = prev - curr
                elif item == '*':
                    total = prev * curr
                else:
                    total = prev // curr
                stack.append(total)
        return stack.pop()

if __name__ == '__main__':
    solution = Solution()
    print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
