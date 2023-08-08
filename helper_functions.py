import sys
import time
import constants

def print_slowly(str, color=constants.colors.PURPLE, pause=0.1):
    '''
    Prints the passed string in the passed color with the passed interval.
    The defaults are purple and 0.1 seconds.'''
    print(color)  # Sets the color
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush(),
        time.sleep(pause)
    print(constants.colors.ENDCOLOR)  # Ends the color effect

def print_text(text, color=constants.colors.PURPLE,
                highlight_color=constants.colors.GREEN, 
                max_width=constants.MIN_TERM_SIZE_COLS, pause=0.005, newline=True):
    '''
    Prints text within the limits of the terminal width
    color: the base text color
    highlight_color: the color of highlighted text surrounded by brackets []
    pause: The pause between each character in seconds
    newline: True adds an extra newline at the end, Flase omits it.
    '''
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if '[NL]' in word:
            lines.append(current_line.strip())
            current_line = word
        elif '[CR]' in word:
            lines.append(current_line.strip())
            current_line = word
        elif len(current_line) + len(word) + 1 <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    text = ' \n'.join(lines)
    text = text.replace('[NL]', '\n')
    text = text.replace('[CR]', '')
    text = text.replace('[',highlight_color)
    text = text.replace(']', color)
    print_slowly(text, color=color, pause=pause)
    if newline:
        print()
