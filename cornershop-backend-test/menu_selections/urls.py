from django.urls import path

from .views import (
    MenuSelectionCreateView,
    MenuSelectionDetailView,
    TodaysMenuSelectionListView,
)

app_name = "menuselections"
urlpatterns = [
    path(
        "<uuid:uuid>/",
        MenuSelectionCreateView.as_view(),
        name="menuselection-create",
    ),
    path(
        "menuselection/today",
        TodaysMenuSelectionListView.as_view(),
        name="menuselection-todaylist",
    ),
    path(
        "menuselection/<int:id>",
        MenuSelectionDetailView.as_view(),
        name="menuselection-detail",
    ),
]
