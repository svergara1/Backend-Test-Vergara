from django import forms

from menus.models import MenuOption

from .models import MenuSelection


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
