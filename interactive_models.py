from datetime import datetime
from framework.pages.practice_form import PracticeForm as PracticeForm_Hybrid
from framework.pages.practice_form_standard_pom import PracticeForm as PracticeForm_Standard

from selenium_essentials.core.helpers.driver_helper import DriverHelper

driver = DriverHelper.get_driver("extended_chrome", install=True)
hybrid_practice_form = PracticeForm_Hybrid(driver)
standard_practice_form = PracticeForm_Standard(driver, navigate_to=False)

print("\n\n--- Welcome to the interactive demo! ---\n")
print("You can now call 'hybrid_practice_form' and perform actions!")
print("\nTry something like: hybrid_practice_form.first_name = 'Sophia'")
