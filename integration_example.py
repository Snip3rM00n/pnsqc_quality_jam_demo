from framework.pages.practice_form import PracticeForm
from selenium_essentials.core.helpers.driver_helper import DriverHelper


config = {"base_uri": "https://demoqa.com"}

driver = DriverHelper.get_driver("chrome", install=False)

practice_form = PracticeForm(driver, config)
