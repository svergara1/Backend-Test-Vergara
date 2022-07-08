import datetime

from django import forms

from menus.models import Menu, MenuOption


class DateInput(forms.DateInput):
    input_type = "date"


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            "menu_date",
        ]
        widgets = {"menu_date": DateInput()}

    def clean(self):
        if Menu.objects.filter(menu_date=datetime.date.today()).exists():
            raise forms.ValidationError("Today's menu is already created")


class MenuOptionModelForm(forms.ModelForm):
    class Meta:
        model = MenuOption
        fields = ["description"]
