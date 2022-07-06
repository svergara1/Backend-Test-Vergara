from django.test import TestCase
from django.urls import reverse

from menu_selections.tests import baker_recipes as menu_selection_recipes


class MenuSelectionUrlTest(TestCase):
    def test_menu_selection_create_url(self):
        menu = menu_selection_recipes.menu_today.make()
        response = self.client.get(
            reverse("menuselections:menuselection-create", args=[menu.uuid])
        )
        self.assertEqual(response.status_code, 200)

    def test_menu_selection_list_url(self):
        response = self.client.get(reverse("menuselections:menuselection-todaylist"))
        self.assertEqual(response.status_code, 200)

    def test_menu_selection_detail_url(self):
        menu_selection = menu_selection_recipes.menu_selection.make()
        response = self.client.get(
            reverse("menuselections:menuselection-detail", args=[menu_selection.id])
        )
        self.assertEqual(response.status_code, 200)
