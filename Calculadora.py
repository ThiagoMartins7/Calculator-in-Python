# Import operator data

import operator

# Added the possibilities of calculation

dict_operators = {

    '%': operator.mod,
    '/': operator.truediv,
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,

}

# The order that python will read the code

print('Enter the number'
number1=int(input())

print('Enter the operator')
operator=input()

print('Enter the number')
number2=int(input())

# How will the calculation be done

print(dict_operators[operator](number1, number2))
