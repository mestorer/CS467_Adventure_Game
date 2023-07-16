import sys
import time
import constants

def print_slowly(str, pause=0.1):
    print('\033[95m')
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush(),
        time.sleep(pause)
    print('\033[0m')

def print_long_text(text, max_width=constants.MIN_TERM_SIZE_COLS):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            print(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
        print(current_line.strip())
    print()