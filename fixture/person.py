from selenium.webdriver.common.by import By
from model.person import Person

class PersonHelper:

    def __init__(self, app):
        self.app = app

    def test_addperson(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_add_page()
        self.create_person(Person(firstname="Dastan", middlename="Ergaly", nickname="Dastish", birthYear="2000"))
        self.logout()

    def test_add_emp_person(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_add_page()
        self.create_person(Person(firstname="", middlename="", nickname="", birthYear=""))
        self.logout()

    def create_person(self, person):
        wd = self.app.wd
        wd.find_element(By.NAME, "firstname").send_keys(person.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").send_keys(person.middlename)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(person.nickname)
        wd.find_element(By.NAME, "bday").click()
        dropdown = wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '6']").click()
        wd.find_element(By.NAME, "bday").click()
        wd.find_element(By.NAME, "bmonth").click()
        dropdown = wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
        wd.find_element(By.NAME, "bmonth").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(person.birthYear)
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

    def open_add_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def delete(self):
        wd = self.app.wd
        self.app.open_home_page()
        # click checkbutton
        wd.find_element(By.NAME, "selected[]").click()
        # click delete button
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete']").click()
        wd.switch_to_alert().accept()