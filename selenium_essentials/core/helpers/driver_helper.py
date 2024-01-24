import os

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium_driver_updater import DriverUpdater

from selenium_essentials.core.extensions.extended_web_driver import ExtendedChromeDriver


class DriverHelper:
    supported_browsers = {
        "chrome": {"class": Chrome, "install_name": DriverUpdater.chromedriver},
        "extended_chrome": {"class": ExtendedChromeDriver, "install_name": DriverUpdater.chromedriver}
    }

    @staticmethod
    def browser_supported(browser: str):
        return browser in DriverHelper.supported_browsers.keys()

    @staticmethod
    def get_extensions_list():
        current_dir = os.path.dirname(__file__)
        ext_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "..", "chrome_extensions"))

        files = os.listdir(ext_dir) if os.path.isdir(ext_dir) else []

        return [os.path.join(ext_dir, file) for file in files if file.endswith(".crx")]


    @staticmethod
    def get_driver(browser: str, install: bool = True, update: bool = True):
        driver_detail = DriverHelper.supported_browsers[browser]

        if install:
            DriverHelper._install_driver(driver_detail["install_name"], update)

        options = Options()
        extension_files = DriverHelper.get_extensions_list()

        for file in extension_files:
            options.add_extension(file)

        driver = driver_detail["class"](options=options)

        return driver


    @staticmethod
    def _install_driver(browser_type: str, update: bool):
        venv_dir = os.environ.get("VIRTUAL_ENV")
        bin_dir = os.path.join(venv_dir, "bin")

        DriverUpdater.install(browser_type, path=bin_dir, upgrade=update)
