from django import forms

from menu_selections import services as menu_selection_services
from menu_selections.models import MenuSelection
from menus.models import MenuOption

# from .services import can_order_todays_meal


class MenuSelectionModelForm(forms.ModelForm):
    class Meta:
        model = MenuSelection
        fields = [
            "employee_firstname",
            "employee_lastname",
            "employee_id",
            "selection",
            "extra_large",
            "specification",
        ]

    def __init__(self, *args, **kwargs):
        uuid = kwargs.pop("uuid")
        super(MenuSelectionModelForm, self).__init__(**kwargs)
        self.fields["selection"].queryset = MenuOption.objects.filter(menu__uuid=uuid)

    def clean(self):
        if not menu_selection_services.can_order_todays_meal():
            raise forms.ValidationError("It's too late to order.")
