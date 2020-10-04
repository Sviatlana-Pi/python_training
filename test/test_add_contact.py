# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.method import Method

@pytest.fixture
def app(request):
    fixture = Method()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_enter_contact(app):
    app.login(username = "admin", password = "secret")
    app.contact_creation(Contact(firstname ="Anton", middlename = "Wiktor", lastname = "Lund", nickname = "alund", title = "Cola", company = "Coca Cola", address = "Kungsgatan 11, lgh 4", home = "City",
                              mobile = "46(67)324-23-23", work = "test", fax = "41", email = "test@gmail.com", email2 = "test1@gmail.com", homepage = "www.tut.by", email3 = "test2@gmail.com", bday = "5",
                              bmonth = "January", byear = "1980", new_group = "group1", notes = "Test note", phone2 = "123123132", address2 = "adress 2", ayear = "1990", amonth = "January", aday = "5"))
    app.logout()

