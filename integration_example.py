from framework.pages.practice_form import PracticeForm
from selenium_essentials.core.helpers.driver_helper import DriverHelper


config = {"base_uri": "https://demoqa.com"}

driver = DriverHelper.get_driver("extended_chrome", install=False)
practice_form = PracticeForm(driver, config)

print("\n\n--- Welcome to the interactive demo! ---\n")
print("You can now call 'practice_form' and perform actions!")
print("\nTry something like: practice_form.first_name = 'Sophia'")
