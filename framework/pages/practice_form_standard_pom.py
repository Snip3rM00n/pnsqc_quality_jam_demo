import os

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_essentials.core.helpers.collection_helpers import CollectionHelpers
from selenium_essentials.core.helpers.general_helpers import GeneralHelpers
from selenium_essentials.objects.bases.base_page import BasePage


class PracticeForm(BasePage):

    @property
    def relative_uri(self):
        return "automation-practice-form"

    def page_to_load(self):
        return self.first_name_element is not None and self.last_name_element is not None

    def post_navigation_actions(self):
        self._remove_ads()

        if len(self._header_group_elements) > 0:
            self._header_group_elements[0].click()

        GeneralHelpers.wait_for(self._ready_to_scroll, time_out_in_seconds=5, throw_on_timeout=False)
        self.driver.execute_script(script="window.scrollBy(0, 200);")

    def _remove_ads(self):
        current_dir = os.path.dirname(__file__)
        script_file = os.path.join(current_dir, "scripts", "removeAds.js")

        with open(script_file, "r") as reader:
            script = reader.read()

        self.driver.execute_script(script)

    @property
    def _header_group_elements(self):
        return self.driver.find_elements(By.CLASS_NAME, "group-header")

    @property
    def _item_8_element(self):
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "item-8"))

    def _ready_to_scroll(self):
        return self._item_8_element is not None and self._item_8_element.is_displayed()

    @property
    def first_name_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "firstName"))

    @property
    def last_name_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "lastName"))

    @property
    def email_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "userEmail"))

    @property
    def male_gender_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "gender-radio-1"))

    @property
    def male_gender_click_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements_by_attribute("for", "gender-radio-1"))

    @property
    def female_gender_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "gender-radio-2"))

    @property
    def female_gender_click_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements_by_attribute("for", "gender-radio-2"))

    @property
    def other_gender_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "gender-radio-3"))

    @property
    def other_gender_click_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements_by_attribute("for", "gender-radio-3"))

    @property
    def mobile_number_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "userNumber"))

    @property
    def date_of_birth_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "dateOfBirthInput"))

    @property
    def subjects_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "subjectsInput"))

    @property
    def sports_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "hobbies-checkbox-1"))

    @property
    def reading_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "hobbies-checkbox-2"))

    @property
    def music_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "hobbies-checkbox-3"))

    @property
    def current_address_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "currentAddress"))

    @property
    def state_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "state"))

    @property
    def city_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "city"))

    def fill_out_form(self, first_name: str, last_name: str, email: str, gender: str, phone_number: str, dob: str,
                      subjects: "[str]", hobbies: "[str]", address: str, state: str, city: str):
        self.first_name_element.clear()
        self.first_name_element.send_keys(first_name)

        self.last_name_element.clear()
        self.last_name_element.send_keys(last_name)

        self.email_element.clear()
        self.email_element.send_keys(email)

        self.mobile_number_element.clear()
        self.mobile_number_element.send_keys(phone_number)

        if gender.lower() == "male":
            self.male_gender_element.click()
        elif gender.lower() == "female":
            self.female_gender_element.click()
        else:
            self.other_gender_element.click()

        self.date_of_birth_element.send_keys(dob)

        for subject in subjects:
            self.subjects_element.send_keys(subject)

        for hobby in hobbies:
            if hobby.lower() == "sports":
                self.sports_element.click()
            elif hobby.lower() == "reading":
                self.reading_element.click()
            elif hobby.lower() == "music":
                self.music_element.click()

        self.current_address_element.clear()
        self.current_address_element.send_keys(address)

        self.state_element.click()
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{state}')]").click()

        self.city_element.click()
        self.driver.find_element(By.XPATH, f"//*[contains(text(), '{city}')]").click()
