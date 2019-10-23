import keyboard
import time
import random
import threading


# Get the opposite of the chosen key so we can revert the last camera movement a little
# and so it looks like a human did it
def get_revert(choice):
    if choice == 'a':
        revert = 'd'
        return revert
    elif choice == 'd':
        revert = 'a'
        return revert
    elif choice == 'w':
        revert = 's'
        return revert
    elif choice == 's':
        revert = 'w'
        return revert


def send_keys():
    key_array = ['a', 'd', 'w', 's']
    # Pick a random rotation direction
    key_choice = random.choice(key_array)
    # Pick 2 random press lengths
    random_length = random.randint(1, 9)
    random_length2 = random.randint(1, 9)
    # for debug: keyboard.send('shift+3+space')
    # Send however many keystrokes we generated above.
    for i in range(random_length):
        keyboard.send(key_choice)
    for i in range(random_length2):
        # get the key to revert the camera movement
        revert_key = get_revert(key_choice)
        keyboard.send(revert_key)


def start_antikick():
    # Get a random execution delay for the timer to send keystrokes.
    random_delay = random.randint(60, 120)
    print(f'Random Delay chosen: {random_delay} seconds. Waiting now...')
    timer = threading.Timer(random_delay, send_keys)
    timer.start()
    while True:
        # if the timer is not active, start a new one
        if not timer.is_alive():
            random_delay = random.randint(60, 120)
            print(f'Random Delay chosen: {random_delay} seconds. Waiting now...')
            timer = threading.Timer(random_delay, send_keys)
            timer.start()
        # if q is pressed, pause the script.
        if keyboard.is_pressed('q'):
            timer.cancel()
            print('Pausing script. Press "s" to resume anti-kick. Use Ctrl+C or close the window to quit the program.')
            break
    # wait for the s key to be pressed to resume execution
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
