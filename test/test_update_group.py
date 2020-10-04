# -*- coding: utf-8 -*-
from model.group import Group

def test_update_first_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.update_first_group(Group(name="group2", header="new header2", footer="group footer2"))
    app.session.logout()