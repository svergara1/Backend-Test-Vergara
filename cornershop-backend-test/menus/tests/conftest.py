import pytest

from model_bakery import baker

from menus.tests import baker_recipes as menu_recipes


@pytest.fixture
def todays_menu():
    return menu_recipes.menu_today.make()


@pytest.fixture
def menu_option():
    return menu_recipes.menuoption_arroz_carne.make()
