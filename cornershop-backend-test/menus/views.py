import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from menu_selections import services as menuselection_services
from menus import services as menu_services

from .forms import MenuModelForm, MenuOptionModelForm
from .models import Menu, MenuOption


class MenuCreateView(LoginRequiredMixin, CreateView):
    template_name = "menus/menu_create.html"
    form_class = MenuModelForm
    queryset = Menu.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)


class MenuListView(LoginRequiredMixin, ListView):
    template_name = "menus/menu_list.html"
    queryset = Menu.objects.all().order_by("-menu_date")


class MenuDetailView(LoginRequiredMixin, DetailView):
    template_name = "menus/menu_detail.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Menu, id=id_)

    def get_context_data(self, **kwargs):
        kwargs["menuoptions"] = MenuOption.objects.filter(menu__id=self.kwargs["id"])
        return super().get_context_data(**kwargs)


class MenuOptionCreateView(LoginRequiredMixin, CreateView):
    template_name = "menuoptions/menuoption_create.html"
    form_class = MenuOptionModelForm
    queryset = MenuOption.objects.all()

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Menu, id=_id)

    def form_valid(self, form):
        menu = self.get_object()
        form.instance.menu = menu
        return super().form_valid(form)


class MenuOptionUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "menuoptions/menuoption_create.html"
    form_class = MenuOptionModelForm
    queryset = Menu.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(MenuOption, id=id_)

    def form_valid(self, form):
        return super().form_valid(form)


def delete_menuoption_view(request, id):
    menuoption = get_object_or_404(MenuOption, id=id)
    menuoption.delete()
    return redirect("menus:menu-detail", id=menuoption.menu.id)


def home_view(request):
    todays_menu = menu_services.get_todays_menu()
    can_still_order_by_time = menuselection_services.can_order_todays_meal()
    context = {
        "todays_menu": todays_menu,
        "can_still_order_by_time": can_still_order_by_time,
    }
    return render(request, "home.html", context)


def send_slack_message_view(request, uuid):
    menu_services.send_slack_message_to_employees(uuid)
    return redirect("/")
