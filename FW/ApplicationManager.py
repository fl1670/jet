from FW.WEB.AnyPage import AnyPage
from FW.WEB.MainPage import MainPage
from FW.WEB.images.Images import Images
from FW.WEB.waitingFW import waitingFW
from FW.ExternalApp.DriverInstance import DriverInstance


class ApplicationManager:

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.waiting = waitingFW(self)

        self.any_page = AnyPage(self)
        self.main_page = MainPage(self)
        self.images = Images(self)
