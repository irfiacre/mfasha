from seleniumbase import Driver
import time
from bs4 import BeautifulSoup

class SeleniumBaseTools:
    """ 
    Gets the contact details of the chosen person
    """

    def __init__(self, web_url: str = "https://urubutopay.rw"):
        """ 
        Initialize a the web driver instance to be used

        Args:
            web_url (str): The URL that has to be opened (default: 'https://urubutopay.rw')

        Returns:
            bool: True if the web url was opened successfully, else False.
        """
        self.driver = Driver(uc=True)
        self.driver.get(web_url)
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
        # return self  # allow chaining

    def close(self):
        """
        Close the browser session gracefully.
        """
        self.driver.quit()


# if __name__ == "__main__":
#     tester = SeleniumBaseToolChain()  # opens browser once
#     # html = tester.get_body_content_page_source()
#     # print(html)  # just preview part of the source
#     time.sleep(3)
#     print(tester.click_xpath('Accept').get_body_content_page_source())
#     tester.close()
