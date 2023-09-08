import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from get_random_videos import YoutubeVideoRandomiser

yt = YoutubeVideoRandomiser(num_of_videos=1)

print(yt.f_mark_z())

"""
print(random_url)
#### SEND THE EMAIL WITH THE URL

subject = "random video generated for you to watch"

body = f"Here is a video you can watch today {random_url}"

recipient = "matirsw@gmail.com"

mail = Email_Handler()

mail.send_email(subject=subject, body=body, recipient=recipient)

"""

