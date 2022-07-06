from unittest import mock

import pytest

from menus import services as menu_services
from menus.exceptions import MenuDoesNotExistException
from menus.tests import baker_recipes as menu_recipes


@mock.patch("menus.services.asynchronous_slack_message.delay")
@pytest.mark.django_db
def test_asynchronous_slack_message_to_employees(mock_asynchronous_slack_message):
    mock_asynchronous_slack_message.assert_not_called()
    menu_services.asynchronous_slack_message.delay("Slack text")
    mock_asynchronous_slack_message.assert_called_once()


@pytest.mark.django_db
def test_get_todays_menu():
    result = menu_services.get_todays_menu()
    assert result == None
    todays_menu = menu_recipes.menu_today.make()
    result = menu_services.get_todays_menu()
    assert result == todays_menu


@pytest.mark.django_db
def test_get_menu_by_id(todays_menu):
    result = menu_services.get_menu_by_id(menu_id=todays_menu.id)
    assert result == todays_menu


@pytest.mark.django_db
def test_get_menu_by_id_doesnt_exist():
    with pytest.raises(MenuDoesNotExistException):
        menu_services.get_menu_by_id(menu_id=-1)


@pytest.mark.django_db
def test_get_menu_option_by_id(menu_option):
    result = menu_services.get_menu_option_by_id(menu_option_id=menu_option.id)
    assert result == menu_option
