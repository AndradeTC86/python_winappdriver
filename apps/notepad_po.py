from appium.webdriver.common.appiumby import AppiumBy

class NotepadPO():
    def __init__(self, wd):
        self.driver = wd

    def minimize_button(self):
        return self.driver.find_element(AppiumBy.NAME, "Minimizar")

    def maximize_button(self):
        return self.driver.find_element(AppiumBy.NAME, "Maximizar")

    def close_button(self):
        return self.driver.find_element(AppiumBy.NAME, "Fechar")

    def menu_file(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "File")

    def menu_edit(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Edit")

    def menu_view(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "View")

    def text_editor(self):
        return self.driver.find_element(AppiumBy.NAME, "Editor de texto")

    def dialog_save_button(self):
        return self.driver.find_element(AppiumBy.NAME, "Salvar")

    def dialog_dont_save_button(self):
        return self.driver.find_element(AppiumBy.NAME, "Não salvar")

    def dialog_cancel_button(self):
        return self.driver.find_element(AppiumBy.NAME, "Cancelar")

