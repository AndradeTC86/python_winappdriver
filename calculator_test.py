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

    def test_subtraction(self):
        print("subtraction")

    def test_multiplication(self):
        print("multiplication")

    def test_division(self):
        print("division")