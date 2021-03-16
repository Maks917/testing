# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from model.person import Person

class TestAddperson():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addperson(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_add_page()
    self.create_person(Person(firstname="Dastan", middlename="Ergaly", nickname="Dastish",birthYear="2000"))
    self.logout()

  def test_add_emp_person(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_add_page()
    self.create_person(Person(firstname="", middlename="", nickname="", birthYear=""))
    self.logout()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def create_person(self, person):
    self.driver.find_element(By.NAME, "firstname").send_keys(person.firstname)
    self.driver.find_element(By.NAME, "middlename").click()
    self.driver.find_element(By.NAME, "middlename").send_keys(person.middlename)
    self.driver.find_element(By.NAME, "nickname").click()
    self.driver.find_element(By.NAME, "nickname").send_keys(person.nickname)
    self.driver.find_element(By.NAME, "bday").click()
    dropdown = self.driver.find_element(By.NAME, "bday")
    dropdown.find_element(By.XPATH, "//option[. = '6']").click()
    self.driver.find_element(By.NAME, "bday").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    dropdown = self.driver.find_element(By.NAME, "bmonth")
    dropdown.find_element(By.XPATH, "//option[. = 'February']").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    self.driver.find_element(By.NAME, "byear").click()
    self.driver.find_element(By.NAME, "byear").send_keys(person.birthYear)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

  def open_add_page(self):
    self.driver.find_element(By.LINK_TEXT, "add new").click()

  def login(self, username, password):
    self.driver.find_element(By.NAME, "user").send_keys(username)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_home_page(self):
    self.driver.get("http://localhost/addressbook/addressbook/")
    self.driver.set_window_size(974, 1040)
  
