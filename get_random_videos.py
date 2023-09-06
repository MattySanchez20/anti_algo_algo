import random
import time

from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

favourite_youtubers = ["CodyKo", "KitchenNightmares"]

random_youtuber = random.choice(favourite_youtubers)

url = f"https://www.youtube.com/@{random_youtuber}/videos"

options = Options()

# detach means it allows chrome to run in a seperate window (set to true)
options.add_experimental_option("detach", True)

# driver uses google chrome as the web browser
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)

# directing the driver to the desired url
driver.get(url=url)

driver.maximize_window()

try:
    # Scroll to the bottom of the page
    last_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        # Scroll down
        driver.execute_script(
            "window.scrollTo(0, document.documentElement.scrollHeight);"
        )

        # Wait for a short time to allow new content to load
        driver.implicitly_wait(2)

        # Check if the "Accept all" button is present
        accept_button = driver.find_elements(
            By.XPATH, "//button[@aria-label='Accept all']"
        )
        if accept_button:
            accept_button[0].click()  # Click the button to accept cookies (if present)
            break

        new_height = driver.execute_script(
            "return document.documentElement.scrollHeight"
        )
        if new_height == last_height:
            # If no more scrolling is possible, break the loop
            break
        last_height = new_height
finally:
    pass

driver.refresh()

popular_button_html = """
//yt-formatted-string[@class='style-scope yt-chip-cloud-chip-renderer']
"""

popular_button_element = driver.find_element(By.XPATH, popular_button_html)

popular_button_element.click()

########################################## scroll to load more videos

# Replace 'your_scroll_amount' with the desired scroll amount (e.g., 2, 3, etc.)
scroll_amount = 2

# Calculate the number of scrolls based on the scroll amount
num_scrolls = 10  # Total number of scrolls you want to perform

for _ in range(num_scrolls):
    # Scroll down
    for _ in range(scroll_amount):
        actions = ActionChains(driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()

    # Wait briefly after scrolling
    time.sleep(0.5)  # Adjust this value if needed

########################################

thumbnail_href_inside = """
//a[@class="yt-simple-endpoint inline-block style-scope ytd-thumbnail"]
"""

thumnail_elements = driver.find_elements(by=By.XPATH, value=thumbnail_href_inside)

random_video_urls = list()

for element in thumnail_elements:
    href_value = element.get_attribute("href")
    if href_value is not None:
        random_video_urls.append(href_value)

driver.quit()

random_url = random.choices(k=5, population=random_video_urls)


class YoutubeVideoRandomiser:
    
    def __init__(
        self,
        favourite_youtubers: List[str] = ['CodyKo', "KitchenNightmares"], 
        num_of_videos: int = 5
        ) -> None:
        self.favourite_youtubers = favourite_youtubers
        self.num_of_videos = num_of_videos
        
    def _create_driver():
        options = Options()

        # detach means it allows chrome to run in a seperate window (set to true)
        options.add_experimental_option("detach", True)

        # driver uses google chrome as the web browser
        driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
        )
        
        return driver
        
    def _handle_t_and_c(self, driver, xpath_to_button: str):
        try:
        # Scroll to the bottom of the page
            last_height = driver.execute_script("return document.documentElement.scrollHeight")

            while True:
            # Scroll down
                driver.execute_script(
                "window.scrollTo(0, document.documentElement.scrollHeight);"
                )

                # Wait for a short time to allow new content to load
                driver.implicitly_wait(2)

                # Check if the "Accept all" button is present
                accept_button = driver.find_elements(
                By.XPATH, xpath_to_button
                )
                if accept_button:
                    accept_button[0].click()  # Click the button to accept cookies (if present)
                    break

                new_height = driver.execute_script(
                "return document.documentElement.scrollHeight"
                )
                if new_height == last_height:
                    # If no more scrolling is possible, break the loop
                    break
                    last_height = new_height
        finally:
            pass

        driver.refresh()
    
    def _scroll_down(self, driver, scroll_amount: int = 2, num_scrolls: int = 10, sleep_duration: float = 0.5):
        """
        ### Replace 'your_scroll_amount' with the desired scroll amount (e.g., 2, 3, etc.)

        ### Calculate the number of scrolls based on the scroll amount
        
        Total number of scrolls you want to perform
        """

        for _ in range(num_scrolls):
        # Scroll down
            for _ in range(scroll_amount):
                actions = ActionChains(driver)
                actions.send_keys(Keys.PAGE_DOWN).perform()

            # Wait briefly after scrolling
            time.sleep(sleep_duration)  # Adjust this value if needed
            
    def _obtain_random_videos(self, thumbnail_href_xpath: str):

        thumnail_elements = driver.find_elements(by=By.XPATH, value=thumbnail_href_xpath)

        random_video_urls = list()

        for element in thumnail_elements:
            href_value = element.get_attribute("href")
            if href_value is not None:
                random_video_urls.append(href_value)

        driver.quit()

        random_url = random.choices(k=5, population=random_video_urls)
        
        return random_url