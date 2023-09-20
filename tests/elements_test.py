import random
import pytest
from pages.elements_page import CheckBoxPage, TextBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, UpLoadAndDownLoadPage, DynamicPropertiesPage


class TestElements:

    class TestTextBox:

        def test_text_box(self, driver):

            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_perm_addr = text_box_page.check_filled_form()
            assert full_name == output_name, "Имя не совпадает"
            assert email == output_email, "Имайл не совпадает"
            assert current_address == output_cur_addr, "Текущий адрес не совпадает"
            assert permanent_address == output_perm_addr, "Постоянный адрес не совпадает"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(
                driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            assert input_checkbox == output_result, "Чекбоксы не совпадают c выбранными"

    class Test_RadioButton:

        @pytest.mark.xfail(reason='must be failed')
        def test_radiobutton(self, driver):
            radiobutton_page = RadioButtonPage(
                driver, 'https://demoqa.com/radio-button')
            radiobutton_page.open()
            radiobutton_page.click_on_the_radiobutton('yes')
            output_yes = radiobutton_page.get_output_result()
            radiobutton_page.click_on_the_radiobutton('impressive')
            output_impressive = radiobutton_page.get_output_result()
            radiobutton_page.click_on_the_radiobutton('no')
            output_no = radiobutton_page.get_output_result()
            assert output_yes == 'Yes', 'YES have not been SELECTED'
            assert output_impressive == 'Impressive', 'Impressive have not been SELECTED'
            assert output_no == 'No', 'NO have not been SELECTED'

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            assert new_person in table_result

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result

        def test_web_table_update_info(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "The person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == 'No rows found'

        @pytest.mark.xfail(reason='must be failed')
        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(
                driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [
                5, 10, 20, 25, 50, 100], 'The number of rows in the table has not been changed or has changed incorrectly'

    class TestButtonsPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open()
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == "You have done a double click", "The double click button was not pressed"
            assert right == "You have done a right click", "The right click button was not pressed"
            assert click == "You have done a dynamic click", "The dynamic click button was not pressed"

    class TestLinksPage:

        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, 'the link is broken or url is incorrect'

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link(
                'https://demoqa.com/bad-request')
            assert response_code == 400, "the link works or the status code is 400"

    class TestUpLoadAndDownLoad:

        def test_upload_file(self, driver):
            upload_download_page = UpLoadAndDownLoadPage(
                driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result

        def test_download_file(self, driver):
            upload_download_page = UpLoadAndDownLoadPage(
                driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True

    class TestDynamicPropertiesPage:

        def test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_changed_of_color()
            assert color_after != color_before

        def test_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear = dynamic_properties_page.check_appear_button()
            assert appear is True

        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(
                driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable = dynamic_properties_page.check_enable_button()
            assert enable is True
