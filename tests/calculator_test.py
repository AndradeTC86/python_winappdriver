import unittest
from appium import webdriver
from apps import calc_po
from appium.options.windows import WindowsOptions

class CalculatorTest(unittest.TestCase):

    calc_session = None
    calc = None

    def setUp(self):
        options = WindowsOptions()
        options.platform_name = 'Windows'
        options.device_name = 'WindowsPC'
        options.app = 'Microsoft.WindowsCalculator_8wekyb3d8bbwe!App'
        self.calc_session = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            options=options
        )
        self.calc = calc_po.CalcPO(self.calc_session)

    def tearDown(self):
        self.calc_session.quit()

    def test_addition(self):
        self.calc.get_num_button("1").click()
        self.calc.get_operator_button("plus").click()
        self.calc.get_num_button("7").click()
        self.calc.get_operator_button("equal").click()
        self.assertEqual(self.calc.get_display_results(), "8")

    def test_subtraction(self):
        self.calc.get_num_button("9").click()
        self.calc.get_operator_button("minus").click()
        self.calc.get_num_button("1").click()
        self.calc.get_operator_button("equal").click()
        self.assertEqual(self.calc.get_display_results(), "8")

    def test_multiplication(self):
        self.calc.get_num_button("8").click()
        self.calc.get_operator_button("multiply").click()
        self.calc.get_num_button("4").click()
        self.calc.get_operator_button("equal").click()
        self.assertEqual(self.calc.get_display_results(), "32")

    def test_division(self):
        self.calc.get_num_button("8").click()
        self.calc.get_operator_button("divide").click()
        self.calc.get_num_button("4").click()
        self.calc.get_operator_button("equal").click()
        self.assertEqual(self.calc.get_display_results(), "2")