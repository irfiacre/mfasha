from seleniumbase import BaseCase
from seleniumbase import Driver
import time
import os
from datetime import datetime

WEB_URL = "https://iradukunda.dev/"
DIST_PATH = "dist"

class BaseTestCase(BaseCase):
    def __init__(self, testName, *args, **kwargs):
        super().__init__(testName, *args, **kwargs)
        current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.reportFile = f"test_report_{current_timestamp}.txt"
        self.testName = testName

    def setUp(self):
        super().setUp()

    def tearDown(self):
        self.save_teardown_screenshot()
        super().tearDown()


class HelperBase(BaseTestCase):

    def open_webapp(self):
        try:
            self.maximize_window()
            time.sleep(2)
            self.open(WEB_URL)
            time.sleep(1)
        except Exception as e:
            self.fail(f"Test failed due to unexpected error: {e}")

    def save_artifacts(self, dir_name: str = "home"):
        try:
            dirname = f'{DIST_PATH}/{dir_name}'
            os.makedirs(dirname, exist_ok=True)
            self.save_screenshot(f'{dirname}/image.png')
            page_source = self.get_page_source()
            self.save_data_as(page_source, "index.html", dirname)

        except Exception as e:
            self.fail(f"Test failed due to unexpected error: {e}")
