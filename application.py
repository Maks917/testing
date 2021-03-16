from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(20)

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def return_to_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "group page").click()

    def create_group(self, group):
        self.open_groups_page()
        # init grop creation
        self.wd.find_element(By.NAME, "new").click()
        # fill group firm
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").click()
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").click()
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element(By.NAME, "submit").click()

    def open_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()

    def login(self, username, password):
        self.open_home_page()
        self.wd.set_window_size(974, 1040)
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").click()
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        self.wd.get("http://localhost/addressbook/addressbook/")

    def destroy(self):
        self.wd.quit()