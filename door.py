from game_object import GameObject
import sys
import time
import constants as const

class Door(GameObject):
    def __init__(self, file_name, data):
        super().__init__(file_name)
        self.name = data['name']
        self.is_locked = data['is_locked']  # Initial state of the door
        self.locked_message = data['locked_message']
        self.unlocked_after_key_message = data['unlocked_after_key_message']
        self.unlocked_message = data['unlocked_message']
        # 'key' is the item that unlocks the transition to the next room
        self.key = data['key']
        self.type = data['type']
        self.opening_count = 0

    def try_to_open(self, player):
        '''
        Returns a True or False if the door unlocks and the appropriate
        message for printing'''
        move_player = True
        if self.is_locked and not self.key in player.inventory:
            message = self.locked_message
            self.animate_door(locked=True, 
                              key=False)
            move_player = False
        elif self.is_locked and self.key in player.inventory:
            message = self.unlocked_after_key_message
            self.animate_door(locked=True, key=True)
            self.is_locked = False
            self.opening_count += 1
        else:
            message = self.unlocked_message
            self.animate_door(locked=False, key=False)
            self.opening_count += 1
        return move_player, message

    def animate_door(self, locked = True, key = False):
        sys.stdout.flush()
        if self.type == 'door':
            app = const.door_approaching
            at = const.door_at
            opening = const.door_opening
            opened = const.door_open
            flash = self.flash_knob
        elif self.type == 'door_badge':
            app = const.door_badge_approaching
            at = const.door_badge_at
            opening = const.door_badge_opening
            opened = const.door_badge_open
            flash = self.flash_badge_sensor
        elif self.type == 'elevator':
            app = const.elevator_approaching
            at = const.elevator_at
            opening = const.elevator_opening
            opened = const.elevator_open
            flash = self.flash_badge_sensor
        else:
            return
        approaching = app if self.opening_count < 1 else at
        if self.opening_count > 1:
            opening = opened
        if locked and not key:
            self.show_animation(approaching, save_curr_pos=True)
            flash(locked=True)
        elif locked and key:
            self.show_animation(approaching, save_curr_pos=True)
            flash(locked=False)
            self.show_animation(opening, save_curr_pos=False)
        elif self.opening_count < 2:
            self.show_animation(approaching, save_curr_pos=True)
            self.show_animation(opening, save_curr_pos=False)
        else:
            pass

    def show_animation(self, frames, frame_duration=0.1, save_curr_pos = True):
        if save_curr_pos:
            sys.stdout.write("\033[s")  # Save current cursor position
        for frame in frames:
            sys.stdout.write("\033[u")  # Restore cursor to the saved position
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(frame_duration)
        sys.stdout.flush()

    def flash_badge_sensor(self, locked, frame_duration=0.1):
        color = const.colors.RED if locked else const.colors.GREEN
        for x in range(5):
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{color}\033[6B\033[14C" + '[]')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{const.colors.NOCOLOR}\033[6B\033[14C" + '[]')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
        sys.stdout.flush()

    def flash_knob(self, locked, frame_duration=0.1):
        color = const.colors.RED if locked else const.colors.GREEN
        for x in range(5):
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{color}\033[6B\033[10C" + 'O')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{const.colors.NOCOLOR}\033[6B\033[10C" + 'O')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
        sys.stdout.flush()
