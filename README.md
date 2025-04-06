# automated-Instagram-DM-
This Python script reads Instagram usernames and messages from a CSV file, then uses pyautogui to automatically send each message as a direct message (DM) on Instagram. The user must open the Instagram DM page before the script starts. It simulates human typing and clicking, making it look more natural.

Reads the CSV file
It loads usernames and messages using pandas.

Waits for you to open Instagram
You get a few seconds to switch to the Instagram DM screen.

Clicks the search bar
It uses pyautogui to click where the search bar is (you set the coordinates).

Types the username
It types the username, waits, and presses Enter to open the chat.

Sends the message
It types the message and hits Enter to send it.

Repeats for all users
It loops through every row in the CSV and sends messages one by one.
