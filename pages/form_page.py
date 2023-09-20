import os
from generator.generator import generated_file
from generator.generator import genereted_persons
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators
from selenium.webdriver.common.keys import Keys


class FormPage(BasePage):
    Locators = FormPageLocators()

    def fill_fields_and_submit(self):
        person = next(genereted_persons())
        file_name, path = generated_file()
        self.element_is_visible(
            self.Locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(
            self.Locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(self.Locators.GENDER).click()
        self.element_is_visible(self.Locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.Locators.SUBJECT).send_keys('Maths')
        self.element_is_visible(self.Locators.SUBJECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.Locators.HOBBIES).click()
        self.element_is_present(self.Locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.Locators.CURRENT_ADRESS).send_keys(
            person.current_address)
        self.element_is_visible(self.Locators.SELECT_STATE).click()
        self.element_is_visible(
            self.Locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.Locators.SELECT_CITY).click()
        self.element_is_visible(
            self.Locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.Locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_presents(self.Locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data
