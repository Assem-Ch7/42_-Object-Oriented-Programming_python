def r(days_to_harvest: int, i: int) -> None:
    if i < days_to_harvest:
        print("Day", i + 1)
        r(days_to_harvest, i + 1)
    else:
        print("Harvest time!")


def ft_count_harvest_recursive():
    days_to_harvest = input("Days until harvest: ")
    r(int(days_to_harvest), 0)
