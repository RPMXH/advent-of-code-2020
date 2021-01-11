# available_buses = ["29", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "41",
#                    "x", "x", "x", "x", "x", "x", "x", "x", "x", "661", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
#                    "x", "x", "13", "17", "x", "x", "x", "x", "x", "x", "x", "x", "23", "x", "x", "x", "x", "x", "x",
#                    "x", "521", "x", "x", "x", "x", "x", "37", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
#                    "x", "19"]

available_buses = ['7', '13', 'x', 'x', '59', 'x', '31', '19']


def filter_fun(variable):
    try:
        int_variable = int(variable)
        return True
    except:
        return False


def map_fun(variable):
    return int(variable)


filtered_buses = filter(filter_fun, available_buses)
int_buses = list(map(map_fun, filtered_buses))
int_buses.sort()

departure_bus = 0
departure_diff = 0
while departure_bus == 0:
    for bus in int_buses:
        if (earliest_departure + departure_diff) % bus == 0:
            departure_bus = bus
            break

    if departure_bus == 0:
        departure_diff += 1

print(departure_bus * departure_diff)
