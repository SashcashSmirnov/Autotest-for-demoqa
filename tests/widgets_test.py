from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, TooltipsPage, MenuPage
from selenium.webdriver.support.ui import WebDriverWait


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(
                driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian(
                'first')
            second_title, second_content = accordian_page.check_accordian(
                'second')
            third_title, third_content = accordian_page.check_accordian(
                'third')
            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0

    class TestAutoComplete:
        def test_fill_multi_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(
                driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_list_in_multi()
            assert colors == colors_result

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(
                driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            assert count_value_before != count_value_after

        def test_fill_single_complete(self, driver):
            autocomplete_page = AutoCompletePage(
                driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result


class TestDatePickerPage:

    def test_change_date(self, driver):
        date_picker_page = DatePickerPage(
            driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date()
        assert value_date_before != value_date_after

    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(
            driver, 'https://demoqa.com/date-picker')
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        assert value_date_before != value_date_after


class TestSliderPage:
    def test_slider(self, driver):
        slider = SliderPage(driver, 'https://demoqa.com/slider')
        slider.open()
        before, after = slider.change_slider_value()
        assert before != after


class TestProgressBarPage:
    def test_progress_bar(self, driver):
        progress_bar = ProgressBarPage(
            driver, 'https://demoqa.com/progress-bar')
        progress_bar.open()
        before, after = progress_bar.change_progress_bar_value()
        assert before != after


class TestTabsPage:
    def test_tabs(self, driver):
        tabs = TabsPage(driver, 'https://demoqa.com/tabs')
        tabs.open()
        data = []
        data = tabs.check_tabs()
        print(data)


class TestToolTipsPage:
    def test_tooltips(self, driver):
        tooltips = TooltipsPage(driver, 'https://demoqa.com/tool-tips')
        tooltips.open()
        button_text, field_text, contrary_text, section_text = tooltips.check_tool_tips()
        assert button_text == 'You hovered over the Button', 'hover missing or incorrect content'
        assert field_text == 'You hovered over the text field', 'hover missing or incorrect content'
        assert contrary_text == 'You hovered over the Contrary', 'hover missing or incorrect content'
        assert section_text == 'You hovered over the 1.10.32', 'hover missing or incorrect content'


class TestMenuPage:
    def test_menu_items(self, driver):
        menu_page = MenuPage(driver, 'https://demoqa.com/menu')
        menu_page.open()
        data = menu_page.check_menu()
        print(data)
