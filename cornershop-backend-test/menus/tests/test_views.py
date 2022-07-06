import datetime
from unittest import mock

import pytest
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from menus import services as menu_services
from menus import views as menu_views
from menus.exceptions import MenuDoesNotExistException
from menus.models import Menu, MenuOption
from menus.tests import baker_recipes as menu_recipes


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="nora", email="nora@cornershop.com", password="abcd1234"
        )
        self.client.login(username="nora", password="abcd1234")

    def test_menu_create_view(self):
        date_time_obj = datetime.datetime.strptime(
            "18/09/22 01:55:19", "%d/%m/%y %H:%M:%S"
        )
        data = {"menu_date": date_time_obj}
        res = self.client.post(
            reverse("menus:menu-create"),
            data,
        )
        self.assertEqual(Menu.objects.last().menu_date, date_time_obj)
        self.assertEqual(res.status_code, 302)


class MenuOptionViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="nora", email="nora@cornershop.com", password="abcd1234"
        )
        self.client.login(username="nora", password="abcd1234")

    @pytest.mark.django_db
    def test_menu_option_create_view(self):
        todays_menu = menu_recipes.menu_today.make()
        data = {"menu": todays_menu, "description": "Arroz con pollo asado"}
        res = self.client.post(
            reverse("menus:menuoption-create", kwargs={"id": todays_menu.id}),
            data,
        )
        self.assertEqual(MenuOption.objects.last().description, "Arroz con pollo asado")
        self.assertEqual(res.status_code, 302)

    def test_menu_option_update(self):
        menu_option = menu_recipes.menuoption_arroz_carne.make()
        response = self.client.post(
            reverse("menus:menuoption-update", kwargs={"id": menu_option.id}),
            {"description": "Lasaña"},
        )
        self.assertEqual(response.status_code, 302)

        menu_option.refresh_from_db()
        self.assertEqual(menu_option.description, "Lasaña")


@mock.patch("menus.services.asynchronous_slack_message.delay")
@pytest.mark.django_db
def test_send_slack_message_view(mock_asynchronous_slack_message, todays_menu):
    mock_asynchronous_slack_message.assert_not_called()
    menu_views.send_slack_message_view(None, todays_menu.uuid)
    mock_asynchronous_slack_message.assert_called_once()
    # SimpleTestCase().assertRedirects(response, "/")


@pytest.mark.django_db
def test_delete_menu_option(menu_option):
    menu_views.delete_menuoption_view(None, menu_option.id)
    with pytest.raises(MenuDoesNotExistException):
        menu_services.get_menu_by_id(menu_id=menu_option.id)
