import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.windows import WindowsOptions

class Calculator_Test(unittest.TestCase):

    calcsession = None
    calcresult = None

    def setUp(self):
        print("setup")
        options = WindowsOptions()
        options.platform_name = 'Windows'
        options.device_name = 'WindowsPC'
        options.app = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
        self.calcsession = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            options=options
        )

    def tearDown(self):
        print("teardown")
        self.calcsession.quit()

    def test_addition(self):
        print("addition")
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num1Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "plusButton").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num7Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.get_display_results(), "8")

    def test_subtraction(self):
        print("subtraction")
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num9Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "minusButton").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num1Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.get_display_results(), "8")

    def test_multiplication(self):
        print("multiplication")
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num9Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "multiplyButton").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num9Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.get_display_results(), "81")

    def test_division(self):
        print("division")
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num8Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "divideButton").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "num4Button").click()
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "equalButton").click()
        self.assertEqual(self.get_display_results(), "2")

    def get_display_results(self):
        text = self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "CalculatorResults").text
        text = text.strip("A exibição é").rstrip(" ").lstrip(" ")
        return text

    def choose_calculator(self, locator):
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "TogglePaneButton").click()
        calculators = self.calcsession.find_elements(AppiumBy.CLASS_NAME, "Microsoft.UI.Xaml.Controls.NavigationViewItem")
        for c in calculators:
            if c.get_attribute("Name") == locator:
                c.click()
                break

    def test_choose_calculator(self):
        self.choose_calculator("Científica Calculadora")

    def choose_calculator_xpath(self, locator):
        self.calcsession.find_element(AppiumBy.ACCESSIBILITY_ID, "TogglePaneButton").click()
        calculators = self.calcsession.find_elements(AppiumBy.XPATH, "//ListItem")
        for c in calculators:
            if c.get_attribute("Name") == locator:
                c.click()
                break

    def test_choose_calculator_xpath(self):
        self.choose_calculator_xpath("Científica Calculadora")