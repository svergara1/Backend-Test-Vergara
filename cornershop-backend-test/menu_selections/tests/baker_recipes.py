import datetime

from model_bakery.recipe import Recipe, foreign_key

from menus.models import Menu, MenuOption

from ..models import MenuSelection

menu_today = Recipe(Menu, menu_date=datetime.datetime.now())

menuoption_arroz_carne = Recipe(
    MenuOption, menu=foreign_key(menu_today), description="Arroz con carne"
)

menu_selection = Recipe(
    MenuSelection,
    employee_firstname="Juan",
    employee_lastname="Perez",
    employee_id=123,
    selection=foreign_key(menuoption_arroz_carne),
    extra_large=True,
    specification="Bien cocido",
)
