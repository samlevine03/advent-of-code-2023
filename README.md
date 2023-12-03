# Advent of Code Solutions

This repository contains my solutions for the [Advent of Code](https://adventofcode.com/) 2023 challenges. Advent of Code is an annual set of Christmas-themed programming puzzles that can be solved in any programming language.

I'm challenging myself to be more **Pythonic**, both at the code level and on a meta level. As such, my goal is to maximize simplicity, readability, and "maintainability." It's worth noting that my solutions will often go through several iterations: first a brute force method, followed by a more efficient (and pythonic) solution. The code you see in each solution will almost never be the code that I used to initially solve each puzzle. 

## Project Structure

The project is organized into separate directories for each day's challenge, a `utils` folder for common functionalities, and a `bin` folder to facilitate easy script execution.

### Day Folders

Each day's challenge has its own folder (e.g., `day1`, `day2`, etc.) containing the solution script for that day.

### Utils Folder

The `utils` folder is a central place for code that is reused across different days. This includes functions for common tasks like reading input data and parsing it into a usable format.

#### Contents of Utils:

- `input_utils.py`: Functions for reading and processing input data.

### Bin Folder

The `bin` folder contains scripts to easily run the solutions for each day. Instead of navigating into each day's folder and running the scripts individually, these helper scripts can be used from the root of the project.

#### Usage:

To run a solution for a specific day, use the following command from the root directory:

```
bin/run day3
```

This command executes the script for Day 3. Replace `day3` with the appropriate day you want to run.

## Getting Started

To get started with running these solutions, clone the repository, and ensure you have Python installed on your system. Each day's script can be run using the helper script in the `bin` folder as described above. That being said, I highly recommend you try out the problems yourself before looking at my solutions! 

## Contributing

Feel free to explore the solutions and suggest any improvements or alternative approaches.
