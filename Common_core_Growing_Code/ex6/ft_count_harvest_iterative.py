def ft_count_harvest_iterative():
    days_to_harvest = input("Days until harvest: ")
    for day in range(int(days_to_harvest)):
        print("Day", day + 1)
    print("Harvest time!")
