import datetime

from django.test import TestCase

import freezegun

from menus.forms import MenuModelForm, MenuOptionModelForm
from menus.models import Menu
from menus.tests import baker_recipes as menu_recipes


class TestMenuForms(TestCase):
    def test_menu_form_valid_data(self):
        date_time_obj = datetime.datetime.strptime("18/09/22", "%d/%m/%y")
        data = {"menu_date": date_time_obj}
        form = MenuModelForm(
            data,
        )
        self.assertTrue(form.is_valid())

    def test_menu_request_form_no_data(self):
        form = MenuModelForm(data={})

        self.assertFalse(form.is_valid())
        # assert that number of fields is correct
        self.assertEqual(len(form.errors), 1)

    @freezegun.freeze_time("2022-09-18")
    def test_menu_form_invalid_menu_already_exists(self):
        data = {"menu_date": datetime.datetime.strptime("18/09/22", "%d/%m/%y")}
        form = MenuModelForm(
            data,
        )
        self.assertTrue(form.is_valid())
        Menu.objects.create(
            menu_date=datetime.datetime.strptime("18/09/22", "%d/%m/%y")
        )
        data = {"menu_date": datetime.datetime.strptime("18/09/22", "%d/%m/%y")}
        form = MenuModelForm(
            data,
        )
        self.assertFalse(form.is_valid())


class TestMenuOptionForms(TestCase):
    def test_menu_form_valid_data(self):
        todays_menu = menu_recipes.menu_today.make()
        data = {"menu": todays_menu, "description": "Arroz con pollo asado"}
        form = MenuOptionModelForm(
            data,
        )
        self.assertTrue(form.is_valid())

    def test_menu_request_form_no_data(self):
        form = MenuOptionModelForm(data={})

        self.assertFalse(form.is_valid())
        # assert that number of fields is correct
        self.assertEqual(len(form.errors), 1)
