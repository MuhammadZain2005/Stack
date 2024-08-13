# Stack Implementation

## Description

The **Stack Implementation** is a Python program that simulates the functionality of a stack data structure. This program supports basic stack operations such as push, pop, and peek, with additional functionalities like step-by-step visualization of the stack operations and performance measurement.

## Features

- **Push/Pop Operations:** Add (`push`) or remove (`pop`) elements from the stack with ease.
- **Step-by-Step Visualization:** Visualize the state of the stack after each `push` and `pop` operation.
- **Peek Operation:** Inspect the top element of the stack without removing it.
- **Performance Measurement:** The program tracks and displays the time taken to perform the stack operations.

## How It Works

The program performs the following steps:

1. **Initialization:** A stack is initialized as an empty list.
2. **Push:** Elements are added to the top of the stack, with an option to visualize the stack after each operation.
3. **Pop:** Elements are removed from the top of the stack, with an option to visualize the stack after each operation.
4. **Peek:** The top element of the stack is displayed without removing it.
5. **Performance Measurement:** The program measures and displays the total time taken to execute all stack operations.

## Usage

### Prerequisites

- Python 3.x

### Running the Program

1. Clone the repository or download the script file `stack.py`.
2. Run the script using Python:

    ```bash
    python stack.py
    ```

3. The program will execute a series of stack operations, visualizing the steps and measuring the time taken.
4. Modify the list or parameters directly in the script to customize the stack behavior.

### Example

```bash
$ python stack.py

Pushed 1: [1]
Pushed 2: [1, 2]
Peek: 2
Popped 2: [1]
Popped 1: []
Is stack empty? True
Time taken for stack operations: 0.000105 seconds
```

## Program Structure

- **`push(item, visualize=False)`**: Adds an item to the top of the stack. If `visualize` is `True`, prints the stack after the operation.
- **`pop(visualize=False)`**: Removes the top item from the stack. If `visualize` is `True`, prints the stack after the operation.
- **`peek()`**: Returns the top item of the stack without removing it.
- **`isEmpty()`**: Checks if the stack is empty.
- **`main()`**: Manages the execution of stack operations, including performance measurement and visualization.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
