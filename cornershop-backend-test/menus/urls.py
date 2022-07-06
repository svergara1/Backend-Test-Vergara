from django.urls import path

from .views import (
    MenuCreateView,
    MenuDetailView,
    MenuListView,
    MenuOptionCreateView,
    MenuOptionUpdateView,
    delete_menuoption_view,
    send_slack_message_view,
)

app_name = "menus"
urlpatterns = [
    path("all/", MenuListView.as_view(), name="menu-list"),
    path("create/", MenuCreateView.as_view(), name="menu-create"),
    path("<int:id>/", MenuDetailView.as_view(), name="menu-detail"),
    path(
        "menuoption/<int:id>/create/",
        MenuOptionCreateView.as_view(),
        name="menuoption-create",
    ),
    path(
        "menuoption/update/<int:id>/",
        MenuOptionUpdateView.as_view(),
        name="menuoption-update",
    ),
    path(
        "menuoption/delete/<int:id>/",
        delete_menuoption_view,
        name="menuoption-delete",
    ),
    path("slack/send/<uuid:uuid>/", send_slack_message_view, name="send-slack-message"),
]
