import sys
import time
import constants

def print_slowly(str, color=constants.colors.PURPLE, pause=0.1):
    print(color)
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush(),
        time.sleep(pause)
    print(constants.colors.ENDCOLOR)

def print_text(text, color=constants.colors.ENDCOLOR, max_width=constants.MIN_TERM_SIZE_COLS, pause=0):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if '\n' in word:
            lines.append(current_line.strip())
            current_line = word + " "
        elif len(current_line) + len(word) + 1 <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    text = ' \n'.join(lines)
    print_slowly(text, color=color, pause=pause)