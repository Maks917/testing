

def test_delete_first_person(app):
    app.session.login(username="admin", password="secret")
    app.person.delete()
    app.session.logout()