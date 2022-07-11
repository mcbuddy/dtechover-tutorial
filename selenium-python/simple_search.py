import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SimpleSearch(unittest.TestCase):
    
    def setUp(self):
        # memulai webdriver session dengan
        # Chromedriver, Geckodriver - Firefox, atau Safaridriver
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        # self.driver = webdriver.Safari()


    def test(self):
        # membuka google site
        self.driver.get("https://www.google.com")

        # membuat variable "search" untuk search bar
        # mencari elment pake name attribute
        searchbar = self.driver.find_element(by=By.NAME, value='q')

        # masuk kata pencarian
        searchbar.send_keys("Indonesia")

        # webdriver tekan enter/return
        searchbar.send_keys(Keys.RETURN)

        # karena mengatasi Firefox race condition
        # kita tambahkan sleep untuk 1 detik sebelum next step
        time.sleep(1)

        # membuat variable "results" untuk hasil pencarian
        # mencari element pake id attribute
        results = self.driver.find_element(by=By.ID, value='search')

        # Simple validasi hasil result ada text yang dicari
        assert("Indonesia - Wikipedia") in results.text
    
    def tearDown(self):
        # menutup webdriver session
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
