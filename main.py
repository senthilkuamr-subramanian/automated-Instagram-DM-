import pandas as pd
import pyautogui
import time
import logging
from typing import Tuple

# Logging config
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_user_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        if 'username' not in df.columns or 'message' not in df.columns:
            raise ValueError("CSV must contain 'username' and 'message' columns.")
        logging.info(f"Loaded {len(df)} entries from {file_path}")
        return df
    except Exception as e:
        logging.error(f"Error loading CSV: {e}")
        raise

def focus_instagram_window(delay: int = 5) -> None:
    logging.info(f"You have {delay} seconds to focus the Instagram DM window...")
    time.sleep(delay)

def click_search_bar(coords: Tuple[int, int]) -> None:
    pyautogui.click(*coords)
    time.sleep(1)

def send_dm(username: str, message: str, coords: Tuple[int, int]) -> None:
    logging.info(f"Preparing to send message to: {username}")
    
    click_search_bar(coords)
    pyautogui.typewrite(username, interval=0.05)
    time.sleep(2)
    
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.typewrite(message, interval=0.04)
    time.sleep(1)
    pyautogui.press('enter')
    logging.info(f"Message successfully sent to {username}")
    time.sleep(2)

def main():
    csv_path = 'data.csv'
    search_bar_coords = (200, 200)  # Replace with your actual search bar position
    
    data = load_user_data(csv_path)
    focus_instagram_window()

    for _, row in data.iterrows():
        send_dm(row['username'], row['message'], search_bar_coords)

    logging.info("All messages sent successfully!")

if __name__ == '__main__':
    main()
