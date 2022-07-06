from django import forms

from .models import Menu, MenuOption


class DateInput(forms.DateInput):
    input_type = "date"


class MenuModelForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = [
            "menu_date",
        ]
        widgets = {"menu_date": DateInput()}


class MenuOptionModelForm(forms.ModelForm):
    class Meta:
        model = MenuOption
        fields = ["description"]
