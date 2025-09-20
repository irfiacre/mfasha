import time
import unittest
from HelperBase.base import HelperBase


class InspectionPage(HelperBase):

    def get_current_page(self):
        self.open_webapp()
        time.sleep(1)
        self.save_artifacts("landing_page")
        assert(True)

if __name__ == "__main__":
    unittest.main()
