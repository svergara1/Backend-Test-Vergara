import datetime


def can_order_todays_meal() -> bool:
    """
    Determines if time of day restriction is met
    :return: Bool
    """
    if datetime.datetime.now() < datetime.datetime.now().replace(
        hour=11, minute=0, second=0, microsecond=0
    ):
        return True
    return False
