# Generated by Selenium IDE
from model.person import Person


def test_addperson(app):
  app.open_home_page()
  app.session.login(username="admin", password="secret")
  app.person.open_add_page()
  app.person.create_person(Person(firstname="Dastan", middlename="Ergaly", nickname="Dastish",birthYear="2000"))
  app.session.logout()

def test_add_emp_person(app):
  app.open_home_page()
  app.session.login(username="admin", password="secret")
  app.person.open_add_page()
  app.person.create_person(Person(firstname="", middlename="", nickname="", birthYear=""))
  app.session.logout()

