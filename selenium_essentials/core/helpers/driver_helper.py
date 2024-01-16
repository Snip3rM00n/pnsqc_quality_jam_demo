import os

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium_driver_updater import DriverUpdater


class DriverHelper:
    supported_browsers = {
        "chrome": {"class": Chrome, "install_name": DriverUpdater.chromedriver}
    }

    @staticmethod
    def browser_supported(browser: str):
        return browser in DriverHelper.supported_browsers.keys()

    @staticmethod
    def get_driver(browser: str, install: bool = True, update: bool = True):
        driver_detail = DriverHelper.supported_browsers[browser]

        if install:
            DriverHelper._install_driver(driver_detail["install_name"], update)

        options = Options()

        driver = Chrome(options=options)
        #driver = driver_detail["class"](chrome_options=options)

        return driver

    @staticmethod
    def _install_driver(browser_type: str, update: bool):
        venv_dir = os.environ.get("VIRTUAL_ENV")
        bin_dir = os.path.join(venv_dir, "bin")

        DriverUpdater.install(browser_type, path=bin_dir, upgrade=update)
