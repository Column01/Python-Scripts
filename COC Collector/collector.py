import os
import time
import threading

import pyautogui

global running
running = False
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
elixir_path = os.path.join(__location__, "elixir.png")
gold_path = os.path.join(__location__, "gold.png")
dark_elixir_path = os.path.join(__location__, "elixir.png")


def find_gold():
    global running
    detection_value = 0.65
    while running:
        gold_scan = None
        while gold_scan is None:
            if running is not False:
                gold_scan = pyautogui.locateOnScreen(gold_path, confidence=detection_value, grayscale=True)
                if gold_scan is not None:
                    print("Found a gold bubble on screen. Clicking it.")
                    click_point = pyautogui.center(gold_scan)
                    pyautogui.click(click_point.x, click_point.y)
            else:
                return
        print("Waiting 3 seconds then we will start scanning for gold again")       
        time.sleep(3)


def find_elixir():
    global running
    detection_value = 0.65
    while running:
        elixir_scan = None
        while elixir_scan is None:
            if running is not False:
                elixir_scan = pyautogui.locateOnScreen(elixir_path, confidence=detection_value, grayscale=True)
                if elixir_scan is not None:
                    print("Found an elixir bubble on screen. Clicking it.")
                    click_point = pyautogui.center(elixir_scan)
                    pyautogui.click(click_point.x, click_point.y)
            else:
                return
        print("Waiting 3 seconds then we will start scanning for the elixir again.")    
        time.sleep(3)
        

def find_dark_elixir():
    global running
    detection_value = 0.60
    while running:
        dark_elixir_scan = None
        while dark_elixir_scan is None:
            if running is not False:
                dark_elixir_scan = pyautogui.locateOnScreen(dark_elixir_path, confidence=detection_value, grayscale=True)
                if dark_elixir_scan is not None:
                    print("Found a dark elixir bubble on screen. Clicking it.")
                    click_point = pyautogui.center(dark_elixir_scan)
                    pyautogui.click(click_point.x, click_point.y)
            else:
                return
        print("Waiting 3 seconds then we will start scanning for dark elixir again.")    
        time.sleep(3)
            
            
def main():
    global running
    running = True
    gold_thread = threading.Thread(target=find_gold)
    gold_thread.start()
    elixir_thread = threading.Thread(target=find_elixir)
    elixir_thread.start()
    dark_elixir_thread = threading.Thread(target=find_dark_elixir)
    dark_elixir_thread.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        running = False
        quit("Recieved keyboard interrupt. Closing script...")


if __name__ == "__main__":
    main()
