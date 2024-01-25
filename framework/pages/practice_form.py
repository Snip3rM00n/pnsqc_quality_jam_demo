import os
import sys
from datetime import datetime

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from framework.wrappers.checkable import CheckableElement
from framework.wrappers.custom_select_element import CustomSelectElement
from framework.wrappers.multi_value_item import MultiValueItem, MultiValueTextBox
from selenium_essentials.core.helpers.collection_helpers import CollectionHelpers
from selenium_essentials.core.helpers.general_helpers import GeneralHelpers
from selenium_essentials.objects.bases.base_page import BasePage


class PracticeForm(BasePage):

    @property
    def relative_uri(self):
        return "automation-practice-form"

    def page_to_load(self):
        return self._first_name_element is not None and self._last_name_element is not None

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
    def _first_name_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "firstName"))

    @property
    def first_name(self):
        return self._first_name_element.get_attribute("value")

    @first_name.setter
    def first_name(self, value):
        if self.first_name != value:
            self._first_name_element.clear()
            self._first_name_element.send_keys(value)

    @property
    def _last_name_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "lastName"))

    @property
    def last_name(self):
        return self._last_name_element.get_attribute("value")

    @last_name.setter
    def last_name(self, value):
        if self.last_name != value:
            self._last_name_element.clear()
            self._last_name_element.send_keys(value)

    @property
    def _email_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "userEmail"))

    @property
    def email(self):
        return self._email_element.get_attribute("value")

    @email.setter
    def email(self, value):
        if self.email != value:
            self._email_element.clear()
            self._email_element.send_keys(value)

    # region - Male Gender Element

    @property
    def _male_gender_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "gender-radio-1")

    @property
    def male(self) -> bool:
        return self._male_gender_element.is_checked

    @male.setter
    def male(self, value):
        if self.male != value:
            self._male_gender_element.click()

    # endregion

    # region - Female Gender Element

    @property
    def _female_gender_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "gender-radio-2")

    @property
    def female(self) -> bool:
        return self._female_gender_element.is_checked

    @female.setter
    def female(self, value):
        if self.female != value:
            self._female_gender_element.click()

    # endregion

    # region - Other Gender Element
    @property
    def _other_gender_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "gender-radio-3")

    @property
    def other(self) -> bool:
        return self._other_gender_element.is_checked

    @other.setter
    def other(self, value):
        if self.other != value:
            self._other_gender_element.click()

    # endregion

    @property
    def _mobile_number_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "userNumber"))

    @property
    def mobile_number(self):
        return self._mobile_number_element.get_attribute("value")

    @mobile_number.setter
    def mobile_number(self, value):
        if self.mobile_number != value:
            self._mobile_number_element.clear()
            self._mobile_number_element.send_keys(value)

    @property
    def _date_of_birth_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "dateOfBirthInput"))

    @property
    def date_of_birth(self):
        value = self._date_of_birth_element.get_attribute("value")
        return datetime.strptime(value, "%d %b %Y")

    @date_of_birth.setter
    def date_of_birth(self, value: datetime):
        date_value = value.strftime("%d %b %Y")
        if self.date_of_birth != date_value:
            select_all = f"{Keys.COMMAND}A" if sys.platform == "darwin" else f"{Keys.CONTROL}A"
            self._date_of_birth_element.send_keys(select_all)

            self._date_of_birth_element.send_keys(date_value)
            self._date_of_birth_element.send_keys(Keys.ESCAPE)

    @property
    def _subjects_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "subjectsInput"))

    @property
    def _subjects_list_parent(self) -> WebElement:
        return CollectionHelpers.first_or_none(
            self.driver.find_elements(By.CLASS_NAME, "subjects-auto-complete__value-container")
        )

    @property
    def _subject_element_list(self) -> "[WebElement]":
        return self._subjects_list_parent.find_elements(By.CLASS_NAME, "subjects-auto-complete__multi-value")

    @property
    def _subject_models(self):
        return [MultiValueItem(element) for element in self._subject_element_list]

    @property
    def subjects(self):
        return MultiValueTextBox(self._subject_models, self._subjects_element)

    @property
    def _sports_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "hobbies-checkbox-1")

    @property
    def sports(self) -> bool:
        return self._sports_element.is_checked

    @sports.setter
    def sports(self, value):
        if self.sports != value:
            self._sports_element.click()

    @property
    def _reading_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "hobbies-checkbox-2")

    @property
    def reading(self) -> bool:
        return self._reading_element.is_checked

    @reading.setter
    def reading(self, value):
        if self.reading != value:
            self._reading_element.click()

    @property
    def _music_element(self) -> CheckableElement:
        return CheckableElement(self.driver, "hobbies-checkbox-3")

    @property
    def music(self) -> bool:
        return self._music_element.is_checked

    @music.setter
    def music(self, value):
        if self.music != value:
            self._music_element.click()

    @property
    def _current_address_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "currentAddress"))

    @property
    def current_address(self):
        return self._current_address_element.get_attribute("value")

    @current_address.setter
    def current_address(self, value):
        if self.current_address != value:
            self._current_address_element.clear()
            self._current_address_element.send_keys(value)

    @property
    def _state_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "state"))

    @property
    def _state_select_element(self) -> CustomSelectElement:
        if self._state_element is not None:
            return CustomSelectElement.from_element(self._state_element)

    @property
    def state(self):
        return self._state_select_element.selected_value

    @state.setter
    def state(self, value):
        self._state_select_element.select(value)

    @property
    def _city_element(self) -> WebElement:
        return CollectionHelpers.first_or_none(self.driver.find_elements(By.ID, "city"))

    @property
    def _city_select_element(self) -> CustomSelectElement:
        if self._city_element is not None:
            return CustomSelectElement.from_element(self._city_element)

    @property
    def city(self):
        return self._city_select_element.selected_value

    @city.setter
    def city(self, value):
        self._city_select_element.select(value)

    def fill_out_form(self, first_name: str, last_name: str, email: str, gender: str, phone_number: str, dob: datetime,
                      subjects: "[str]", hobbies: "[str]", address: str, state: str, city: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        setattr(self, gender.lower(), True)

        self.mobile_number = phone_number
        self.date_of_birth = dob

        self.subjects.extend(subjects)

        for hobby in hobbies:
            if hasattr(self, hobby.lower()):
                setattr(self, hobby.lower(), True)

        self.current_address = address
        self.state = state
        self.city = city
