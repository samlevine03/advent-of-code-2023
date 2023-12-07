import requests
import sys
import os
from dotenv import load_dotenv

def fetch_puzzle_input(day_num, session_cookie):
    url = f"https://adventofcode.com/2023/day/{day_num}/input"
    headers = {'Cookie': f'session={session_cookie}'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return f"Unable to fetch puzzle input. (HTTP Status: {response.status_code})"

    return response.text

def main():
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(dotenv_path)

    if len(sys.argv) > 1:
        day_num = sys.argv[1]
    else:
        print("Day number not provided. Using default day 4 for testing.")
        exit(1)

    session_cookie = os.environ.get('ADVENT_OF_CODE_SESSION')
    puzzle_input = fetch_puzzle_input(day_num, session_cookie)

    print(puzzle_input)

if __name__ == "__main__":
    main()
