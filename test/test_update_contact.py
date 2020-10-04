# -*- coding: utf-8 -*-
from model.contact import Contact

def test_update_first_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.update_first_contact(Contact(firstname="AntonNew", middlename="WiktorNew", lastname="LundNew", nickname="alundNew", title="ColaNew",
                               company="Coca ColaNew", address="Kungsgatan 11New, lgh 4", home="CityNew",
                               mobile="46(67)324-23-231", work="testNew", fax="411", email="testNew@gmail.com",
                               email2="test1New@gmail.com", homepage="www.tutNew.by", email3="test2New@gmail.com", bday="6",
                               bmonth="February", byear="1981", new_group="group1", notes="Test noteNew",
                               phone2="1231231321", address2="adress 21", ayear="1920", amonth="February", aday="6"))

    app.session.logout()