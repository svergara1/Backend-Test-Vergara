import datetime
import json

from celery import shared_task
from django.conf import settings

import requests

from menus.exceptions import MenuDoesNotExistException, MenuOptionDoesNotExistException
from menus.models import Menu, MenuOption


def get_menu_by_id(menu_id: int) -> Menu:
    """
    Get Menu by Menu ID
    :param menu_id: Menu ID
    :return: Menu
    :raises MenuDoesNotExistException: Menu does not exist
    """
    try:
        return Menu.objects.get(id=menu_id)
    except Menu.DoesNotExist:
        raise MenuDoesNotExistException(status_code=404, error_code="MENU_NOT_FOUND")


def get_menu_option_by_id(menu_option_id: int) -> MenuOption:
    """
    Get Menu option by Menu option ID
    :param menu_option_id: MenuOption ID
    :return: MenuOption
    :raises MenuOptionDoesNotExistException: Menu does not exist
    """
    try:
        return MenuOption.objects.get(id=menu_option_id)
    except MenuOption.DoesNotExist:
        raise MenuOptionDoesNotExistException(
            status_code=404, error_code="MENU_OPTION_NOT_FOUND"
        )


def get_todays_menu() -> Menu:
    """
    Get Today's Menu
    :return: Menu
    :raises MenuDoesNotExistException: Menu does not exist
    """
    try:
        return Menu.objects.get(menu_date__gte=datetime.date.today())
    except Menu.DoesNotExist:
        return None


@shared_task
def asynchronous_slack_message(text):
    """
    Sends asynchronous slack messages
    """
    url = settings.SLACK_WEBHOOK
    data = {"text": text}
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=json.dumps(data), headers=headers)


def send_slack_message_to_employees(order_uuid):
    """
    Create text for slack message and send call asynchronous method
    :param order_uuid: UUID
    """
    menuoptions = MenuOption.objects.filter(menu__uuid=order_uuid)
    text = "Hola!\n Dejo el menú de hoy: http://127.0.0.1:8000/menu/{}\n".format(
        order_uuid
    )
    count = 1
    for option in menuoptions.iterator():
        text += "Option {}: ".format(count) + option.description + "\n"
        count += 1
    text += "\nTengan lindo día!"
    asynchronous_slack_message.delay(text=text)


def delete_menuoption(id):
    menuoption = MenuOption.objects.get(id=id)
    menuoption.delete()
