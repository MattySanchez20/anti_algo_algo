import random
import time
from typing import List

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class YoutubeVideoRandomiser:
    def __init__(
        self,
        favourite_youtubers: List[str] = ["CodyKo", "KitchenNightmares"],
        num_of_videos: int = 5,
    ) -> None:
        self.favourite_youtubers = favourite_youtubers
        self.num_of_videos = num_of_videos

    @staticmethod
    def _create_driver():

        chrome_options = Options()

        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        return driver

    def _handle_t_and_c(
        self, driver, xpath_to_button: str = "//button[@aria-label='Accept all']"
    ):
        try:
            # Scroll to the bottom of the page
            last_height = driver.execute_script(
                "return document.documentElement.scrollHeight"
            )

            while True:
                # Scroll down
                driver.execute_script(
                    "window.scrollTo(0, document.documentElement.scrollHeight);"
                )

                # Wait for a short time to allow new content to load
                driver.implicitly_wait(2)

                # Check if the "Accept all" button is present
                accept_button = driver.find_elements(By.XPATH, xpath_to_button)
                if accept_button:
                    accept_button[
                        0
                    ].click()  # Click the button to accept cookies (if present)
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

    def _scroll_down(
        self,
        driver,
        scroll_amount: int = 2,
        num_scrolls: int = 10,
        sleep_duration: float = 0.5,
    ):
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

    def _obtain_random_videos(
        self, driver, thumbnail_href_xpath: str, num_of_videos: int
    ):
        thumnail_elements = driver.find_elements(
            by=By.XPATH, value=thumbnail_href_xpath
        )

        random_video_urls = list()

        for element in thumnail_elements:
            href_value = element.get_attribute("href")
            if href_value is not None:
                random_video_urls.append(href_value)

        driver.quit()

        random_url = random.choices(k=num_of_videos, population=random_video_urls)

        return random_url

    def f_mark_z(self):
        random_youtuber = random.choice(self.favourite_youtubers)

        url = f"https://www.youtube.com/@{random_youtuber}/videos"

        driver = self._create_driver()

        # directing the driver to the desired url
        driver.get(url=url)

        driver.maximize_window()

        self._handle_t_and_c(driver=driver)

        popular_button_html = """
        //yt-formatted-string[@class='style-scope yt-chip-cloud-chip-renderer']
        """

        popular_button_element = driver.find_element(By.XPATH, popular_button_html)

        popular_button_element.click()

        ########################################## scroll to load more videos

        self._scroll_down(driver=driver)

        ########################################

        thumbnail_href_inside = """
        //a[@class="yt-simple-endpoint inline-block style-scope ytd-thumbnail"]
        """

        random_vids = self._obtain_random_videos(
            driver=driver,
            thumbnail_href_xpath=thumbnail_href_inside,
            num_of_videos=self.num_of_videos,
        )

        driver.quit()
        
        video_ids = [video.replace("https://www.youtube.com/watch?v=", "") for video in random_vids]

        embeded_urls = [f"https://www.youtube.com/embed/{_id}?controls=0" for _id in video_ids]

        return embeded_urls
