from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException

class BrowseJobs(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_BrowseCompanies_linktext_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='footer']/div/div[2]/div/a[6]"))

    def test_BrowseCompanies_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='footer']/div/div[2]/div/a[6]")
        self.assertEqual(element.text,"Browse Companies")


    def test_BrowseCompanies_linktext_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='footer']/div/div[2]/div/a[6]")

        try:
            element.click()
        except WebDriverException as e:
            print("Element is not clickable")

    def tearDown(self):
        self.driver.quit()