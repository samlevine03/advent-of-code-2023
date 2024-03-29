# Advent of Code

This repository contains my solutions for the [Advent of Code](https://adventofcode.com/) 2023 challenges. Advent of Code is an annual set of Christmas-themed programming puzzles that can be solved in any programming language.

I'm challenging myself to be more ***Pythonic***, both at the code level and on a meta level. As such, my goal is to maximize simplicity, readability, and "maintainability." It's worth noting that my solutions will often go through several iterations: first a brute force method, followed by a more efficient (and pythonic) solution. The code you see in each solution will almost never be the code that I used to initially solve each puzzle. 

## Rules (for myself)
- No ChatGPT. I'm allowing Copilot since it's a timesaver and helps me avoid syntax errors without actually giving me answers.
- No work-arounds for slow code. By Day 5 naive solutions are becoming too slow or memory intensive. Rather than trying to get around this with libraries like multiprocessing or Cython, I want to focus on improving my underlying approach in vanilla Python. 

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

To create a new folder for a specific day (pre-loaded with utils imported and your input file), use the following command from the root directory:
```
bin/new day3
```

## Stuff I've Learned

Here are some of the highlights:

- **Bash Scripting**: Shell scripts are utilized to automate common tasks, such as creating new challenge folders and running solutions.
- **re**: I've dabbled, but this was *mostly* new to me. Used regular expressions to vastly simplify some solutions where key operations involved parsing text. 


## Getting Started

To get started with running these solutions, clone the repository, and ensure you have Python installed on your system. Then from the root directory, run `bin/setup`. If you have any issues with the scripts, try `chmod +x [bin/script_name]`.

Each day's script can be run using the helper script in the `bin` folder as described above. That being said, I highly recommend you try out the problems yourself before looking at my solutions! 

In order to use `bin/new`, you'll your session cookie to grab your unique input. Open up [Day 1's Input](https://adventofcode.com/2023/day/1/input) and go to your developer tools. You should be able to find your session cookie in Storage -> Cookies. You can also find it in Network -> input -> Request Headers. Save this to your .env as `ADVENT_OF_CODE_SESSION` and you'll be good to go!

## Contributing

Feel free to explore the solutions and suggest any improvements or alternative approaches. I'm still a rookie when it comes to Pythonic programming (and meta programming). If you have any feed back on how I could structure things, let me know!
