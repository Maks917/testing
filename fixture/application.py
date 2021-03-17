from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.person import PersonHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.person = PersonHelper(self)

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/addressbook/")

    def destroy(self):
        self.wd.quit()