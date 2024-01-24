from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from selenium_essentials.core.extensions.extended_web_driver import BaseExtendedWebDriver

from selenium_essentials.core.helpers.general_helpers import GeneralHelpers


class BasePage:

    def __init__(self, driver: "BaseExtendedWebDriver", config: dict = None, navigate_to: bool = True):
        self.driver = driver
        self._config = config

        if navigate_to:
            self.pre_navigation_actions()

            self.nagivate_to()
            GeneralHelpers.wait_for(self.page_to_load)

            self.post_navigation_actions()

    @property
    def base_uri(self):
        return self._config.get("base_uri")

    @property
    def relative_uri(self):
        return ""

    @property
    def url(self):
        return f"{self.base_uri}/{self.relative_uri}"

    def nagivate_to(self):
        self.driver.get(self.url)

    def page_to_load(self):
        return False

    def pre_navigation_actions(self):
        pass

    def post_navigation_actions(self):
        pass
