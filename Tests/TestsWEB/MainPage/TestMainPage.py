import allure
import pytest

from Tests.TestBase import TestBase


@allure.testcase('https://yandex.ru/')
@allure.feature('Web')
@allure.story('Проверка главной страницы (https://yandex.ru/)')
class TestMainPage(TestBase):

    @allure.title('Тест 1 - запарсить значение из кода и вывести на консоль, для слов "погода", “Липецк”, “Лото”')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.parametrize("text", ['погода', 'Липецк', 'Лото'])
    def test_1_main_page(self, text):
        self.APP.main_page.set_text_in_search(text)
        print('\n' + self.APP.main_page.get_text_search_popup())

    @allure.title('Тест 2')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://yandex.ru/')
    @pytest.mark.webTest
    @pytest.mark.Smoke
    @pytest.mark.Login
    def test_2_main_page(self):
        assert True is self.APP.main_page.check_link_images()
        assert True is self.APP.main_page.check_link_images2()
        assert 'yandex.ru/images' in self.APP.main_page.get_link_images()

        self.APP.main_page.click_link_images()

        assert 'https://yandex.ru/images/' in self.APP.any_page.get_current_url()



