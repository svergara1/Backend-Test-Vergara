from django.test import TestCase
from django.urls import reverse

from menus.tests import baker_recipes as menu_recipes


class MenuUrlTest(TestCase):
    def test_menu_create_url(self):
        response = self.client.get(reverse("menus:menu-create"))
        self.assertEqual(response.status_code, 302)

    def test_menu_list_url(self):
        response = self.client.get(reverse("menus:menu-list"))
        self.assertEqual(response.status_code, 302)

    def test_menu_detail_url(self):
        menu = menu_recipes.menu_today.make()
        response = self.client.get(reverse("menus:menu-detail", args=[menu.id]))
        self.assertEqual(response.status_code, 302)


class MenuOptionUrlTest(TestCase):
    def test_menu_option_create_url(self):
        menu = menu_recipes.menu_today.make()
        response = self.client.get(reverse("menus:menuoption-create", args=[menu.id]))
        self.assertEqual(response.status_code, 302)

    def test_menu_option_update_url(self):
        menu_option = menu_recipes.menuoption_arroz_carne.make()
        response = self.client.get(
            reverse("menus:menuoption-update", args=[menu_option.id])
        )
        self.assertEqual(response.status_code, 302)

    def test_menu_option_detail_url(self):
        menu_option = menu_recipes.menuoption_arroz_carne.make()
        response = self.client.get(
            reverse("menus:menuoption-delete", args=[menu_option.id])
        )
        self.assertEqual(response.status_code, 302)
