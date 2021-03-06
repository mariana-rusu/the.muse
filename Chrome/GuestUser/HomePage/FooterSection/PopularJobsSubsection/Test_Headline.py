from selenium import webdriver
import unittest
import time

class Headline(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_Headline_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='footer']/div/div[3]/div/h6"))

    def test_Headline_text_is_found(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='footer']/div/div[3]/div/h6")
        self.assertEqual(element.text,"POPULAR JOBS")


    def tearDown(self):
        self.driver.quit()