from appium.webdriver.common.appiumby import AppiumBy

class CalcPO():
    def __init__(self, wd):
        self.driver = wd

    def get_num_button(self, num):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "num" + num + "Button")

    def get_operator_button(self, operator):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, operator + "Button")

    def get_display_results(self):
        text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "CalculatorResults").text
        text = text.strip("A exibição é").rstrip(" ").lstrip(" ")
        return text

