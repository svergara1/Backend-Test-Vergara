import datetime

from model_bakery.recipe import Recipe, foreign_key

from menus.models import Menu, MenuOption

menu_today = Recipe(Menu, menu_date=datetime.date.today())

menuoption_arroz_carne = Recipe(
    MenuOption, menu=foreign_key(menu_today), description="Arroz con carne"
)
