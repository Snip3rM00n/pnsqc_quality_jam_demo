import time
from unittest import TestCase

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium_essentials.core.helpers.driver_helper import DriverHelper
from framework.pages.practice_form_standard_pom import PracticeForm as Standard_POM_Form
from framework.pages.practice_form import PracticeForm as Hybrid_POMLFM_Form


class Test_LogicalFunctionOnly(TestCase):

    def setUp(self):
        self._driver = Chrome()

    def test_populate_some_elements(self):
        self._driver.get("https://demoqa.com/automation-practice-form")
        time.sleep(10)

        self._driver.find_element(By.ID, "firstName").send_keys("Amelia")
        assert self._driver.find_element(By.ID, "firstName").get_attribute("value") == "Amelia"

        self._driver.find_element(By.ID, "lastName").send_keys("Bedelia")
        assert self._driver.find_element(By.ID, "lastName").get_attribute("value") == "Bedelia"

        self._driver.find_element(By.ID, "userEmail").send_keys("maid_2b_literal at email dot com")
        assert self._driver.find_element(By.ID, "userEmail").get_attribute(
            "value") == "maid_2b_literal at email dot com"

        self._driver.find_element(By.CSS_SELECTOR, '*[for="gender-radio-2"').click()
        assert self._driver.find_element(By.ID, "gender-radio-2").is_selected() is True

        self._driver.find_element(By.ID, "state").click()
        time.sleep(1)
        self._driver.find_element(By.XPATH, "//*[contains(text(), 'Haryana')]").click()
        assert self._driver.find_element(By.CSS_SELECTOR, '*[class$="-singleValue"').text == "Haryana"

    def test_something_else(self):
        self.test_populate_some_elements()
        self._driver.find_element(By.ID, "firstName").clear()
        self._driver.find_element(By.ID, "lastName").clear()
        # AND SO ON


class Test_StandardPOM(TestCase):

    def setUp(self):
        self._driver = DriverHelper.get_driver("extended_chrome")

    def test_populate_some_elements(self):
        form_page = Standard_POM_Form(self._driver)

        form_page.first_name_element.send_keys("Amelia")
        assert form_page.first_name_element.get_attribute("value") == "Amelia"

        form_page.last_name_element.send_keys("Bedelia")
        assert form_page.last_name_element.get_attribute("value") == "Bedelia"

        form_page.email_element.send_keys("maid_2b_literal at email dot com")
        assert form_page.email_element.get_attribute("value") == "maid_2b_literal at email dot com"

        form_page.female_gender_click_element.click()
        assert form_page.female_gender_element.is_selected()

        form_page.state_element.click()
        time.sleep(1)
        self._driver.find_element(By.XPATH, "//*[contains(text(), 'Haryana')]").click()
        assert self._driver.find_element(By.CSS_SELECTOR, '*[class$="-singleValue"').text == "Haryana"


class Test_Hybrid_POMLFM(TestCase):

    def setUp(self):
        self._driver = DriverHelper.get_driver("extended_chrome")

    def test_populate_some_elements(self):
        form_page = Hybrid_POMLFM_Form(self._driver)

        form_page.first_name = "Amelia"
        assert form_page.first_name == "Amelia"

        form_page.last_name = "Bedelia"
        assert form_page.last_name == "Bedelia"

        form_page.email = "maid_2b_literal at email dot com"
        assert form_page.email == "maid_2b_literal at email dot com"

        form_page.female = True
        assert form_page.female is True

        form_page.state = "Haryana"
        assert form_page.state == "Haryana"
