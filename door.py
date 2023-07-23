from game_object import GameObject
import sys
import time
import ascii_art.door_animation as door_anim

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
        self.kind = data['kind']
        self.opening_count = 0

    def try_to_open(self, player):
        '''
        Tries to open the door based on player's inventory and door state.
        Returns a tuple of (move_player, message) indicating whether the player 
        can move and the appropriate message to display.
        '''
        move_player = True

        if self.is_locked and self.key not in player.inventory:
            message = self.locked_message
            self.animate_door(locked=True, key=False)
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

    def animate_door(self, locked=True, key=False):
        '''
        Animates the door based on its kind and state.
        '''
        sys.stdout.flush()
        # Determine the animation frames based on door kind
        if self.kind == 'door':
            approaching_anim = door_anim.door_approaching
            at_anim = door_anim.door_at
            opening_anim = door_anim.door_opening
            opened_anim = door_anim.door_open
            flash = self.flash_knob
        elif self.kind == 'door_badge':
            approaching_anim = door_anim.door_badge_approaching
            at_anim = door_anim.door_badge_at
            opening_anim = door_anim.door_badge_opening
            opened_anim = door_anim.door_badge_open
            flash = self.flash_badge_sensor
        elif self.kind == 'elevator':
            approaching_anim = door_anim.elevator_approaching
            at_anim = door_anim.elevator_at
            opening_anim = door_anim.elevator_opening
            opened_anim = door_anim.elevator_open
            flash = self.flash_badge_sensor
        else:
            return

        # Determine the appropriate animation frames based on door state
        approaching_frames = approaching_anim if self.opening_count < 1 \
            else at_anim
        if self.opening_count > 1:
            opening_frames = opened_anim
        else:
            opening_frames = opening_anim

        # Play the animations accordingly
        if locked and not key:
            self.show_animation(approaching_frames, save_curr_pos=True)
            flash(locked=True)
        elif locked and key:
            self.show_animation(approaching_frames, save_curr_pos=True)
            flash(locked=False)
            self.show_animation(opening_frames, save_curr_pos=False)
        elif self.opening_count < 2:
            self.show_animation(approaching_frames, save_curr_pos=True)
            self.show_animation(opening_frames, save_curr_pos=False)
        else:
            pass

    def show_animation(self, frames, frame_duration=0.1, save_curr_pos=True):
        '''
        Displays the given animation frames with a specified frame duration.
        '''
        if save_curr_pos:
            sys.stdout.write("\033[s")  # Save current cursor position
        for frame in frames:
            sys.stdout.write("\033[u")  # Restore cursor to the saved position
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(frame_duration)
        sys.stdout.flush()

    def flash_badge_sensor(self, locked, frame_duration=0.1):
        '''
        Flashes the badge sensor for a few frames to indicate locked/unlocked state.
        '''
        color = door_anim.RED if locked else door_anim.GREEN
        for x in range(5):
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{color}\033[6B\033[14C" + '[]')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{door_anim.NOCOLOR}\033[6B\033[14C" + '[]')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
        sys.stdout.flush()

    def flash_knob(self, locked, frame_duration=0.1):
        '''
        Flashes the knob for a few frames to indicate locked/unlocked state.
        '''
        color = door_anim.RED if locked else door_anim.GREEN
        for x in range(5):
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{color}\033[6B\033[10C" + 'O')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
            sys.stdout.write("\033[u")
            sys.stdout.write(f"{door_anim.NOCOLOR}\033[6B\033[10C" + 'O')
            sys.stdout.write("\033[9B\033[1C")
            sys.stdout.flush()
            time.sleep(frame_duration)
        sys.stdout.flush()
