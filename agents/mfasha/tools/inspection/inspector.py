import time
import random
import unittest
from HelperBase.base import HelperBase


class AutomateMarkItemsAsRead(HelperBase):

    def get_current_page(self):
        self.open_webapp()
        time.sleep(1)
        self.save_artifacts("landing_page")
        assert(True)

if __name__ == "__main__":
    unittest.main()
