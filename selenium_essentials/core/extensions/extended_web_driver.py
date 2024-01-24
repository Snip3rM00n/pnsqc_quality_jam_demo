from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from selenium_essentials.core.helpers.collection_helpers import CollectionHelpers


class BaseExtendedWebDriver(WebDriver):

    def find_element_by_attribute(self, attribute_name, value, equality="=") -> "WebElement":
        return CollectionHelpers.first_or_none(self.find_elements_by_attribute(attribute_name, value, equality))

    def find_elements_by_attribute(self, attribute_name, value, equality="=") -> "[WebElement]":
        return self.find_elements(By.CSS_SELECTOR, f'*[{attribute_name}{equality}"{value}"]')


class ExtendedChromeDriver(BaseExtendedWebDriver, Chrome):
    """
    An extended version of the chrome driver.
    """