import pytest
from django.test import Client, TestCase
from django.urls import reverse

from menu_selections.models import MenuSelection
from menus.tests import baker_recipes as menu_recipes


class MenuSelectionViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    @pytest.mark.django_db
    def test_menu_selection_create_view(self):
        menu_option = menu_recipes.menuoption_arroz_carne.make()
        data = {
            "employee_firstname": "Juan",
            "employee_lastname": "Perez",
            "employee_id": 123,
            "selection": menu_option.id,
            "extra_large": True,
            "specification": "Bien cocido",
        }
        res = self.client.post(
            reverse(
                "menuselections:menuselection-create",
                kwargs={"uuid": menu_option.menu.uuid},
            ),
            data,
        )
        self.assertEqual(res.status_code, 302)
        self.assertEqual(MenuSelection.objects.last().employee_id, 123)
        self.assertEqual(MenuSelection.objects.last().selection, menu_option)
