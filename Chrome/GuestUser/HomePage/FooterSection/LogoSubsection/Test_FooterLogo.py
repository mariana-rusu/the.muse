from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
import requests
from selenium.common.exceptions import WebDriverException

class Logo(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.themuse.com/")
        time.sleep(1)

    def test_Logo_class_is_found(self):

        driver = self.driver
        assert (driver.find_element_by_xpath("//*[@id='footer']/div/div[1]/a"))


    def test_Logo_image_is_found(self):

        driver = self.driver
        example_images = driver.find_elements(By.XPATH, '//div/div[1]/a/img')

        self.verificationErrors = []
        for image in example_images:
            current_link = image.get_attribute("src")
            r = requests.get(current_link)
            try:
                self.assertEqual(r.status_code, 200)
            except AssertionError:
                self.verificationErrors.append(current_link + ' delivered response code of ' + r.status_code)


    def test_Logo_is_clickable(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='footer']/div/div[1]/a")

        try:
            element.click()
        except WebDriverException:
            print("Element is not clickable")

    def test_TheMuseCopyright(self):

        driver = self.driver
        element = driver.find_element_by_xpath("//*[@id='footer']/div/div[1]/div")
        self.assertEqual(element.text,"© 2017 Daily Muse, Inc")



    def tearDown(self):
        self.driver.quit()