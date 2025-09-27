from seleniumbase import Driver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


class SeleniumBaseTools:
    """ 
    Gets the contact details of the chosen person
    """

    def __init__(self):
        """ 
        Initialize the SeleniumBaseTools class with the necessary pages
        """
        self.driver = None

    def start_browser_session(self, web_url: str):
        """
        Starts the browser session successfully.

        Args:
            web_url (str): The URI that has to be opened in the browser session (example: www.google.com).
        """
        self.driver = Driver(uc=True)
        self.driver.uc_open_with_reconnect(web_url, 4)
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

    def scroll(self, direction: str = "DOWN", scroll_amount: int = 1):
        """
        Scroll up or down the page.

        Args:
            direction (str): The direction to scroll to (example: 'DOWN' or 'UP').
            scroll_amount (int): The number of times you want to scroll (example: 1).
        """
        for i in range(scroll_amount):
            if direction == 'UP':
                self.execute_script("window.scrollTo(%s, 0);" % (i * 100))
            else:
                self.execute_script("window.scrollTo(0, %s);" % (i * 100))
        

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