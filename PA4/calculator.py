
# Name: Yuhua Huang
# 6 March 2023
# Creates a calculator and infix to postfix function transforming infixes to posfix for the calculations. And caluate the user's input 


def infix_to_postfix(infix):
        # Create an empty 'opstack' stack for keeping operators.
        opstack = []
        # Create an empty list for output.
        output = []
        # Define operator precedence
        precedence = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
        # Scan the token list from left to right.
        for token in infix:
            # If the token is an operand, append it to the end of the output list.
            if token.isdigit():
                output.append(token)
            # If the token is a left parenthesis, push it on the opstack.
            elif token == '(':
                opstack.append(token)
            # If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed.
            # Append each operator to the end of the output list.
            elif token == ')':
                top_token = opstack.pop()
                while top_token != '(':
                    output.append(top_token)
                    top_token = opstack.pop()
            # If the token is an operator, *, /, +, or -, push it on the opstack.
            # eles then the first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.
            elif token in precedence:
                while opstack and precedence[opstack[-1]] >= precedence[token]:
                    output.append(opstack.pop())
                opstack.append(token)
        # When the input expression has been completely processed, check the opstack.
        # Any operators still on the stack can be removed and appended to the end of the output list.
        while opstack:
            output.append(opstack.pop())
        # Return the postfix expression as a string
        return ' '.join(output)

 

def calculate(infix):
    # Convert the infix expression to postfix
    postfix = infix_to_postfix(infix)
    # Create a stack to evaluate the postfix expression
    stack = []
    # Split the postfix expression into tokens
    tokens = postfix.split()
    # Evaluate the postfix expression
    for token in tokens:
        # If the token is an operand, push it onto the stack
        if token.isdigit():
            stack.append(float(token))
        # If the token is an operator, pop the top two operands from the stack, apply the operator, and push the result back onto the stack
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            # Push the result back onto the stack
            stack.append(result)
    # The final result is the only value remaining on the stack
    return stack.pop()

def main(): #welcoming and asking users to input for the calculation
    print("Welcome to Calculator Program!")
    while True:
        user_input = input("Please enter your expression here. To quit enter 'quit' or 'q': ")
        if user_input.lower() in ['quit', 'q']:
            print("Goodbye!")
            break
        result = calculate(user_input)
        print(result)

if __name__ == '__main__':
    main()
    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0

