from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selenium_essentials.core.helpers.collection_helpers import CollectionHelpers
from selenium_essentials.objects.bases.base_page import BasePage


class PracticeForm(BasePage):

    @property
    def relative_uri(self):
        return "automation-practice-form"

    def page_to_load(self):
        return self._first_name_element is not None and self._last_name_element is not None

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
