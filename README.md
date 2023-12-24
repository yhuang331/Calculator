 Calculator Project

This Python calculator project consists of several files designed to provide a basic calculator functionality with a graphical user interface (GUI). The calculator supports arithmetic operations, infix to postfix conversion, and the construction of an expression tree.

## Files

### `Calculator.py`

Main program responsible for orchestrating the calculator functionalities and interacting with the user. It integrates the ADT tree and stack modules to perform calculations.

### `Tree.py`

This module defines an Abstract Data Type (ADT) for a tree and includes two classes: `BinaryTree` and `ExpTree`. `BinaryTree` provides the basic structure for a binary tree, while `ExpTree` specifically handles expression trees. Expression trees are used in the calculator to represent mathematical expressions.

### `Stack.py`

Another ADT module, this time for a stack. The `Stack` class provides the necessary functionality for a stack data structure, which is crucial for operations like infix to postfix conversion.

### `calculatorGUI.py`

This file utilizes the Tkinter library to create a graphical user interface for the calculator. It implements the visual components of the calculator, allowing users to input expressions and view the results. The GUI also incorporates infix to postfix conversion and expression tree construction for advanced calculations.

## Usage

1. Ensure you have Python installed on your machine.
2. Run `Calculator.py` to launch the calculator.
3. Use the graphical interface to input expressions and perform calculations.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division).
- Infix to postfix conversion for expression handling.
- Construction of expression trees for advanced mathematical operations.

## Contributing

Contributions to enhance or extend the functionality of this calculator project are welcome. If you encounter bugs, have feature requests, or want to contribute code improvements, please open an issue or submit a pull request.

