from seleniumbase import Driver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


class SeleniumBaseTools:
    """ 
    Gets the contact details of the chosen person
    """

    def __init__(self, web_url: str = "https://urubutopay.rw"):
        """ 
        Initialize the SeleniumBaseTools class with the necessary pages

        Args:
            web_url (str): The URL that has to be opened (default: 'https://urubutopay.rw')

        Returns:
            bool: True if the web url was opened successfully, else False.
        """
        self.web_url = web_url
        self.driver = None

    def start_browser_session(self):
        """
        Starts the browser session successfully.
        """
        self.driver = Driver(uc=True)
        self.driver.get(self.web_url)
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)

    def get_body_content_page_source(self) -> str | None:
        """ 
        Gets the current html page source. 

        Returns:
            str | None: Body content of the html page source.
        """
        try:
            if 'body' in (htmlContent := self.driver.get_page_source()):
                parsedHtml = BeautifulSoup(htmlContent, 'html.parser')
                bodyContent = parsedHtml.body
                return str(bodyContent) if bodyContent else None
            return None 
        except Exception as ex:
            print("=== ERROR:", ex)
            return None

    def click_xpath(self, element_xpath: str) -> bool:
        """ 
        Click an element by its xpath

        Args:
            element_xpath (str): The xpath of the element that has to be clicked.

        Returns:
            bool: True when element is clicked else False
        """
        try:
            self.driver.click(element_xpath)
            time.sleep(2)
            return True
        except Exception as ex:
            print("=== ERROR:", ex)
            return False

    def add_text_to_input(self, element_xpath: str, text_to_send: str):
        """
        Adds a text to an input field that is focused on.

        Args:
            element_xpath (str): The xpath of the input field to where the text should be input.
            text_to_send (str): The text that should be added to the input.
        """
        self.driver.send_keys(selector=element_xpath, text=text_to_send)

    def scroll(self, element_xpath: str, direction: str = "DOWN"):
        """
        Scroll up or down the page.

        Args:
            element_xpath (str): The xpath of any element to reference the action.
            direction (str): The direction to scroll to (default: 'DOWN').
        """
        if direction == 'UP':
            self.driver.send_keys(element_xpath, Keys.ARROW_UP)
        else:
            self.driver.send_keys(element_xpath, Keys.ARROW_DOWN)

    def click_enter(self, element_xpath: str):
        """
        Simulates clicking the enter button on a keyboard

        Args:
            element_xpath (str): The xpath of the input field to where to click enter.
        """
        self.driver.send_keys(element_xpath, Keys.ENTER)

    def close(self):
        """
        Close the browser session gracefully.
        """
        self.driver.quit()
        # os.removedirs('downloaded_files')


# if __name__ == "__main__":
#     tester = SeleniumBaseTools('https://youtube.com')  # opens browser once
#     tester.start_browser_session()
#     time.sleep(2)
#     tester.click_xpath('Search')
#     time.sleep(2)
#     tester.add_text_to_input('//*[@id="center"]/yt-searchbox/div[1]/form/input','funny cats')
#     time.sleep(3)
#     tester.click_enter('//*[@id="center"]/yt-searchbox/div[1]/form/input')
#     time.sleep(1)
#     tester.scroll('//*[@id="center"]/yt-searchbox/div[1]/form/input', 'DOWN')
#     tester.close()

# send_keys(Keys.ENTER)