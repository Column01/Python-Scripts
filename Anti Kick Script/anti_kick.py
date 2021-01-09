import keyboard
import time
import random
import threading


revert_dict = {"a": "d", "d": "a", "w": "s", "s": "w"}
key_array = ['a', 'd', 'w', 's']


def get_revert(choice):
    # Get the opposite key to revert our choice
    return revert_dict.get(choice)


def send_keys():
    # Pick a random rotation direction
    key_choice = random.choice(key_array)
    # Get the key to revert the direction
    revert_key = get_revert(key_choice)

    # Send however many keystrokes we generated between 1 and 9 times.
    for _ in range(random.randint(1, 9)):
        keyboard.send(key_choice)
    for _ in range(random.randint(1, 9)):
        keyboard.send(revert_key)


def start_antikick():
    # Get an initial random execution delay for the timer to send keystrokes.
    random_delay = random.randint(60, 120)
    print(f'Random Delay chosen: {random_delay} seconds. Waiting now...')
    timer = threading.Timer(random_delay, send_keys)
    timer.start()
    while True:
        # If the timer is not active, start a new one with a random delay
        if not timer.is_alive():
            random_delay = random.randint(60, 120)
            print(f'Random Delay chosen: {random_delay} seconds. Waiting now...')
            timer = threading.Timer(random_delay, send_keys)
            timer.start()
        # If q is pressed, pause the script.
        if keyboard.is_pressed('q'):
            timer.cancel()
            print('Pausing script. Press "s" to resume anti-kick. Use Ctrl+C or close the window to quit the program.')
            break
    # Wait for the s key to be pressed to resume execution
    try:
        keyboard.wait('s')
        start_antikick()
    except KeyboardInterrupt:
        raise SystemExit


print('Press "s" to start Anti-Kick')
# Wait for the s key to be pressed to start the script.
keyboard.wait('s')
print('Starting Anti-Kick in 3 seconds. Press "q" to pause execution')
time.sleep(3)
start_antikick()
