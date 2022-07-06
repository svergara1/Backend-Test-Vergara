import pytest

import freezegun

from menu_selections import services as menu_selections_services


@pytest.mark.django_db
@freezegun.freeze_time("2022-01-05 10:59:00")
def test_can_order_todays_meal():
    result = menu_selections_services.can_order_todays_meal()
    assert result == True


@pytest.mark.django_db
@freezegun.freeze_time("2022-01-05 11:01:00")
def test_can_not_order_todays_meal():
    result = menu_selections_services.can_order_todays_meal()
    assert result == False
