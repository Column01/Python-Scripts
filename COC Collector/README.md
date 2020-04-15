# Clash of Clans auto resource collector
A Python script to scan your screen for clash of clans resource bubbles from collectors and click them to harvest it.
This does not prevent your from getting kicked when your villagers need a break!

## Dependencies
- [PyAutoGui](https://pypi.org/project/PyAutoGUI/)
- [OpenCV Python](https://pypi.org/project/opencv-python/)

## Usage
1. Install [BlueStacks](https://www.bluestacks.com/)
2. Set your BlueStacks settings up for the proper resolution:
	1. Click the menu button (looks like three horizontal lines)
	2. Click settings
	3. Under "Display", set "Resolution" to `1600 x 900` and DPI to `240 DPI`
3. Log into your google play account and install clash of clans.
4. Load your clash of clans base from your Play games account or from supercell account.
5. Zoom ALL the way out on your base by pressing the down arrow key or by pressing `Ctrl + -` until it is all the way zoomed out.
5. Download this script and the dependencies listed above.
6. Run the script using `python collector.py`
7. It should detect gold, and elixir bubbles (both types) and automatically click them. Dark elixir and normal elixir may trigger each other since they are so similar. I can't find a way around it yet, but it's not a huge deal.

### Notes
- If it doesn't detect one of the resource types, make sure you have the display settings set properly and you are zoomed all the way out.
- If it detects false positives or still doesn't detect a resource type, you may need to tweak the detection percentage in the script. It can be found in the `find_gold`, `find_dark_elixir` and `find_elixir` functions labeled `detection_value`. It must not exceed `1.0` and I don't reccommend anything lower than `0.50`
- The detection might not work on some monitor resolutions. It was designed on a 1080p resolution so any monitor with a lower or higher resolution may not detect the bubble properly. If that is the case, you can copy the image samples I included by zooming all the way out on your base and screenshotting the gold, dark elixir and elixir collection bubbles. Then you just need to rename the files to the same as I have it and it should work fine.