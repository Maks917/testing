from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init grop creation
        wd.find_element(By.NAME, "new").click()
        # fill group firm
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        # click checkbutton
        wd.find_element(By.NAME, "selected[]").click()
        # click delete button
        wd.find_element(By.NAME, "delete").click()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()
