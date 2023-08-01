from game_manager import GameManager

if __name__ == '__main__':
    gm = GameManager()
    while True:
        game = gm.start_game()
        if not game:
            print("\nThanks for playing!\n")
            break