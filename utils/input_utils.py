import os
import inspect

def get_input():
    """
    Get the input from the file.
    """
    # Get the file path of the calling script
    caller_file = inspect.stack()[1].filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))

    # Path to the input file in the same directory as the calling script
    input_file_path = os.path.join(caller_dir, 'input.txt')

    with open(input_file_path, 'r') as f:
        return f.read().splitlines()


def input_to_2d_array(input):
    """
    Convert the input to a 2d array.
    """
    return [list(line) for line in input]