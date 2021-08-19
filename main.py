import subprocess
import pyautogui
import time
import pandas as pandas
from datetime import datetime

def sign_in(meetingid, pswd):
     subprocess.call('C:\Program Files (x86)\Webex\Webex\Applications\ptoneclk.exe')
     time.sleep(10)

     join_btn = pyautogui.locateCenterOnScreen('join_btn.png')
     pyautogui.moveTo(join_btn)
     pyautogui.click()

     meeting_id_btn = pyautogui.locateCenterOnScreen('join_btn_press.png')
     pyautogui.moveTo(meeting_id_btn)
     pyautogui.click()
     pyautogui.write(meetingid)

     click_btn = pyautogui.locateCenterOnScreen('join_click.png')
     pyautogui.moveTo(click_btn)
     pyautogui.click()

sign_in("913055153", "8AmcpK")