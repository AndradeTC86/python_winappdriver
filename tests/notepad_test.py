import unittest
from appium import webdriver
from selenium.webdriver import Keys
from apps import notepad_po
from appium.options.windows import WindowsOptions

class NotepadTest(unittest.TestCase):

    notepad_session = None
    notepad = None

    def setUp(self):
        options = WindowsOptions()
        options.platform_name = 'Windows'
        options.device_name = 'WindowsPC'
        options.app = r'C:\Windows\System32\notepad.exe'
        self.notepad_session = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            options=options
        )
        self.notepad = notepad_po.NotepadPO(self.notepad_session)

    def tearDown(self):
        self.notepad_session.quit()

    def test_note_creation(self):
        self.notepad.text_editor().send_keys("Test Automation with WinAppDriver")
        self.assertEqual(self.notepad.text_editor().text, "Test Automation with WinAppDriver")
        self.notepad.text_editor().send_keys(Keys.CONTROL, "w")
        self.notepad.dialog_cancel_button().click()
        self.assertEqual(self.notepad.text_editor().text, "Test Automation with WinAppDriver")
        self.notepad.text_editor().send_keys(Keys.CONTROL, "w")
        self.notepad.dialog_dont_save_button().click()
