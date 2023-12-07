import requests
from bs4 import BeautifulSoup, NavigableString
import sys

def fetch_instructions(day_num):
    url = f"https://adventofcode.com/2023/day/{day_num}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Invalid day or the day's challenge is not yet available. (HTTP Status: {response.status_code})"

    soup = BeautifulSoup(response.text, 'html.parser')
    instructions = soup.find('article')
    if not instructions:
        return "Instructions not found on the page."

    def process_element(element):
        if isinstance(element, NavigableString):
            return element.strip()
        if element.name == 'code':
            inner_text = ' '.join(process_element(child) for child in element.contents).strip()
            return f"`{inner_text}`"
        elif element.name == 'em':
            inner_text = ' '.join(process_element(child) for child in element.contents).strip()
            return f"*{inner_text}*"
        elif element.name == 'li':
            content = ' '.join(process_element(child) for child in element.contents).strip()
            return f" - {content}"
        elif element.name == 'ul':
            list_items = [process_element(li) for li in element.find_all('li', recursive=False)]
            return '\n'.join(list_items)
        elif element.name == 'pre':
            return f"```\n{element.get_text(strip=True)}\n```"
        else:
            return ' '.join(process_element(child) for child in element.contents)

    text_parts = [process_element(child) for child in instructions.children if not isinstance(child, NavigableString) or child.strip()]
    formatted_text = '\n\n'.join(text_parts).strip()
    return formatted_text


def main():
    if len(sys.argv) > 1:
        day_num = sys.argv[1]
        instructions = fetch_instructions(day_num)
        print(instructions)
    else:
        print("Day number not provided. Please run the script with a day number argument.")

if __name__ == "__main__":
    main()
