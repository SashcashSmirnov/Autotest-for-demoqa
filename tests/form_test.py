import time
from pages.form_page import FormPage


class TestForm:
    class TestFormPage:
        def test_form(self, driver):
            form_page = FormPage(
                driver, 'https://demoqa.com/automation-practice-form')
            form_page.open()
            p = form_page.fill_fields_and_submit()
            result = form_page.form_result()
            assert [p.firstname + " " + p.lastname,
                    p.email] == [result[0], result[1]]
