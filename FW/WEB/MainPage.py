import allure

from FW.WEB.AnyPage import AnyPage


class MainPage(AnyPage):
    _search_input = '//input[@id="text"]'
    _popup_content = '//div[@class="popup__content"]/div/li[1]'
    _images = '//div[@class="home-arrow__tabs "]/div/a[@data-id="images"]'

    def set_text_in_search(self, text):
        self.clear_and_send_keys_by_xpath(self._search_input, text)
        return self

    def get_text_search_popup(self):
        self.manager.waiting.waiting_element_to_be_clickable(self._popup_content)
        return self.get_tag_text(self._popup_content)

    def check_link_images(self):
        return self.check_for_element(self._images)

    def check_link_images2(self):
        return self.check_for_element2(self._images)

    def get_link_images(self):
        return self.get_tag_attribute(self._images, 'href')

    @allure.step('Переходим по ссылке "Картинки"')
    def click_link_images(self):
        self.click_by_xpath(self._images)
        return self.manager.images

