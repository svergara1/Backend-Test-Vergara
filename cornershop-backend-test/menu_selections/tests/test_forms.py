from django.test import TestCase

from menu_selections.forms import MenuSelectionModelForm
from menus.tests import baker_recipes as menu_recipes


class TestForms(TestCase):
    def test_menu_selection_form_valid_data(self):
        menu_option = menu_recipes.menuoption_arroz_carne.make()
        form = MenuSelectionModelForm(
            uuid=menu_option.menu.uuid,
            data={
                "employee_firstname": "Juan",
                "employee_lastname": "Perez",
                "employee_id": 123,
                "selection": menu_option.id,
                "extra_large": True,
                "specification": "Bien cocido",
            },
        )
        self.assertTrue(form.is_valid())

    def test_menu_selection_form_no_data(self):
        menu_option = menu_recipes.menuoption_arroz_carne.make()
        form = MenuSelectionModelForm(uuid=menu_option.menu.uuid, data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)
