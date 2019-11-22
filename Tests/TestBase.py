from FW.ApplicationManager import ApplicationManager
from Data.GroupData import group_data


class TestBase:
    APP = None
    GroupData = None

    def setup_class(self):
        self.APP = ApplicationManager()
        self.GroupData = group_data()

    def teardown_class(self):
        self.APP.driver_instance.stop_Test()

    def setup_method(self):
        self.APP.any_page.open_main_page(self.GroupData.GLOBAL[self.GroupData.branch]['main_page'])

    def teardown_method(self):
        pass
