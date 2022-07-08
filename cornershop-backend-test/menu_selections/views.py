import datetime

from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, DetailView, ListView

from menu_selections.forms import MenuSelectionModelForm
from menu_selections.models import MenuSelection
from menus.models import Menu, MenuOption


# Create your views here.
class MenuSelectionCreateView(CreateView):
    template_name = "menuselection_create.html"
    form_class = MenuSelectionModelForm
    queryset = MenuSelection.objects.all()

    def get_form_kwargs(self):
        kwargs = super(MenuSelectionCreateView, self).get_form_kwargs()
        kwargs.update({"uuid": self.kwargs.get("uuid")})
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs["menu"] = Menu.objects.get(uuid=self.kwargs["uuid"])
        kwargs["menuoption"] = MenuOption.objects.filter(menu=kwargs["menu"])
        return super().get_context_data(**kwargs)


class TodaysMenuSelectionListView(ListView):
    template_name = "menuselection_list.html"
    queryset = MenuSelection.objects.filter(created_at__gte=datetime.date.today())

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class MenuSelectionDetailView(DetailView):
    template_name = "menuselection_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(MenuSelection, id=id_)
