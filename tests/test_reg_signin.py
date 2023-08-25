import unittest
from inspect import currentframe
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Local_Login_Tests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
    """
    def test_signin_success(self):
        self.browser.get("http://127.0.0.1:5000")
        buttons = self.browser.find_elements(By.CSS_SELECTOR, "button")
        #print(buttons)          #debug print
        time.sleep(2)
        buttons[0].click()
        time.sleep(3)
        self.browser.find_element(By.NAME, "username").send_keys("OP")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("abc123")
        time.sleep(2)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(5)

    def test_signin_failure(self):
        self.browser.get("http://127.0.0.1:5000")
        buttons = self.browser.find_elements(By.CSS_SELECTOR, "button")
        #print(buttons)          #debug print
        time.sleep(2)
        buttons[0].click()
        time.sleep(3)
        self.browser.find_element(By.NAME, "username").send_keys("OP")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("ab23")
        time.sleep(2)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(5)
    """
    def test_1_registration_success(self):
        print("Running ", currentframe().f_code.co_name, "...")
        self.browser.get("http://127.0.0.1:5000/registration/")
        time.sleep(2)
        self.browser.find_element(By.NAME, "fname").send_keys("test")
        time.sleep(1)
        self.browser.find_element(By.NAME, "lname").send_keys("0")
        time.sleep(1)
        self.browser.find_element(By.NAME, "username").send_keys("test0")
        time.sleep(1)
        self.browser.find_element(By.NAME, "email").send_keys("tester@test.com")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("abc123")
        time.sleep(2)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(7)

    def test_2_registration_fail_accountExists(self):
        #assumes test_registration_success was already successfully run
        print("Running ", currentframe().f_code.co_name, "...")
        self.browser.get("http://127.0.0.1:5000/registration/")
        time.sleep(2)
        self.browser.find_element(By.NAME, "fname").send_keys("test")
        time.sleep(1)
        self.browser.find_element(By.NAME, "lname").send_keys("0")
        time.sleep(1)
        self.browser.find_element(By.NAME, "username").send_keys("test0")
        time.sleep(1)
        self.browser.find_element(By.NAME, "email").send_keys("tester@test.com")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("abc123")
        time.sleep(2)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(7)

    def test_3_registration_fail_sameusrnm_diffcredentials(self):
        print("Running ", currentframe().f_code.co_name, "...")
        self.browser.get("http://127.0.0.1:5000/registration/")
        time.sleep(2)
        self.browser.find_element(By.NAME, "fname").send_keys("tester")
        time.sleep(1)
        self.browser.find_element(By.NAME, "lname").send_keys("0")
        time.sleep(1)
        self.browser.find_element(By.NAME, "username").send_keys("test0")
        time.sleep(1)
        self.browser.find_element(By.NAME, "email").send_keys("tester0@test.com")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("abc123")
        time.sleep(2)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(7)

    def test_4_registration_success_diffusrnm_sameemail(self):
        #in theory, should still send verification email to same email address
        print("Running ", currentframe().f_code.co_name, "...")
        self.browser.get("http://127.0.0.1:5000/registration/")
        time.sleep(2)
        self.browser.find_element(By.NAME, "fname").send_keys("test")
        time.sleep(1)
        self.browser.find_element(By.NAME, "lname").send_keys("1")
        time.sleep(1)
        self.browser.find_element(By.NAME, "username").send_keys("test1")
        time.sleep(1)
        self.browser.find_element(By.NAME, "email").send_keys("tester@test.com")
        time.sleep(1)
        self.browser.find_element(By.NAME, "password").send_keys("abc123")
        time.sleep(2)
        self.browser.find_element(By.NAME, "password").send_keys(Keys.RETURN)
        time.sleep(7)


if __name__ == '__main__':
    unittest.main(verbosity=2)
