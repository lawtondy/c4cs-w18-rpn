#!/usr/bin/env python3

import operator
import logging
import sys
import math

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def calculate(arg):
    stack = list()
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            if(token == '!'):
                arg1 = stack.pop()
                result = math.factorial(arg1)
                stack.append(result)
            elif(token == '&'):
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arg1 & arg2
                stack.append(result)
            elif(token == '^'):
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arg1 ** arg2
                stack.append(result)
            elif(token == '|'):
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = arg1 | arg2
                stack.append(result)
            elif(token == '~'):
                arg1 = stack.pop()
                result = ~arg1
                stack.append(result)
            elif(token == '?'):
                result  = 0
                while(len(stack) != 0):
                    arg = stack.pop()
                    result += arg
                stack.append(result)
            else:
                function = operators[token]
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = function(arg1, arg2)
                stack.append(result)
        logger.debug(stack)

    if len(stack) != 1:
        raise TypeError
    
    return stack.pop()

def main():
    while True:
        print(calculate(input('rpn calc> ')))

if __name__ == '__main__':
    main()
