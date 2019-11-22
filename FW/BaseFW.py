import allure
from allure_commons.types import AttachmentType

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BaseFW(object):
    time_element_Wait = 30
    driver = None

    def __init__(self, application_manager):
        self.manager = application_manager

    def get_driver(self):
        if self.driver is None:
            self.driver = self.manager.driver_instance.get_driver()
        return self.driver

    @allure.step('Открыть главную страницу')
    def open_main_page(self, main_page):
        title = self.get_driver().current_url
        if main_page not in title:
            self.get_driver().get(main_page)

    @allure.step('click')
    def click_by_xpath(self, locator):
        self.get_driver().find_element_by_xpath(locator).click()

    @allure.step('send_keys')
    def send_keys_by_xpath(self, locator, text):
        self.get_driver().find_element_by_xpath(locator).send_keys(text)

    @allure.step('clear_and_send_keys_by_xpath')
    def clear_and_send_keys_by_xpath(self, locator, text):
        self.clear_by_xpath(locator)
        self.get_driver().find_element_by_xpath(locator).send_keys(text)

    def get_tag_text(self, locator):
        return self.get_driver().find_element_by_xpath(locator).text

    def get_tag_attribute(self, locator, attribute):
        return self.get_driver().find_element_by_xpath(locator).get_attribute(attribute)

    def scroll_to_element(self, locator):
        try:
            temp = self.get_driver().find_element_by_xpath(locator).location_once_scrolled_into_view
            self.get_driver().execute_script("window.scrollBy(" + str(temp['x']) + ", " + str(temp['y']) + ")")
        except StaleElementReferenceException as e:
            self.allure_ElementNotVisibleException(e)

    @allure.step("moveToElement")
    def moveToElement(self, locator):
        actions = ActionChains(self.get_driver())
        element = self.get_driver().find_element_by_xpath(locator)
        actions.move_to_element(element)
        actions.perform()

    @allure.step('Очистка текстового поля')
    def clear_by_xpath(self, locator):
        try:
            self.get_driver().find_element_by_xpath(locator).clear()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    def get_current_url(self):
        return self.get_driver().current_url

    @allure.step('Нажатие правой кнопкой мыши')
    def right_click_dy_xpath(self, locator):
        try:
            self.scroll_to_element(locator)
            actionChains = ActionChains(self.get_driver())
            actionChains.context_click(self.get_driver().find_element_by_xpath(locator)).perform()
        except ElementNotVisibleException as e:
            self.allure_ElementNotVisibleException(e)
        except NoSuchElementException as e:
            self.allure_NoSuchElementException(e)

    @allure.step('refresh_page')
    def refresh_the_page(self):
        self.get_driver().refresh()

    def check_for_element(self, locator):
        try:
            self.get_driver().find_element_by_xpath(locator)
            return True
        except NoSuchElementException:
            return False

    def check_for_element2(self, locator):
        return self.get_driver().find_element_by_xpath(locator).is_displayed()

    @allure.step('screenshot')
    def allure_screenshot(self, driver):
        try:
            allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        except Exception as e:
            self.allure_Exception(e)

    @allure.step("select_element_by_visible_text:")
    def select_element_by_visible_text(self, select_locator, text):
        select = Select(self.get_driver().find_element_by_xpath(select_locator))
        select.select_by_visible_text(text)

    # остановщик теста при ошибке
    @allure.step('ElementNotVisibleException')
    def allure_ElementNotVisibleException(self, ExeptionText):
        assert False

    # остановщик теста при ошибке
    @allure.step('NoSuchElementException')
    def allure_NoSuchElementException(self, ExeptionText):
        assert False

    # остановщик теста при ошибке
    @allure.step('StaleElementReferenceException')
    def allure_StaleElementReferenceException(self, ExeptionText):
        assert False

    # остановщик теста при ошибке
    @allure.step('Exception')
    def allure_Exception(self, Exception):
        assert False
