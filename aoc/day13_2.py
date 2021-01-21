available_buses = ["29", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "41",
                   "x", "x", "x", "x", "x", "x", "x", "x", "x", "661", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                   "x", "x", "13", "17", "x", "x", "x", "x", "x", "x", "x", "x", "23", "x", "x", "x", "x", "x", "x",
                   "x", "521", "x", "x", "x", "x", "x", "37", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
                   "x", "19"]

# available_buses = ['7', '13', 'x', 'x', '59', 'x', '31', '19']
# available_buses = ['17', 'x', '13', '19']
# available_buses = ['67', '7', '59', '61']
# available_buses = ['67', 'x', '7', '59', '61']
# available_buses = ['67', '7', 'x', '59', '61']
# available_buses = ['1789', '37', '47', '1889']

real_buses = []
bus_delay = []

for num, bus in enumerate(available_buses, start=0):
    int_bus = 0
    delay = 0

    try:
        int_bus = int(bus)
    except:
        int_bus = 0

    if int_bus > 0:
        real_buses.append(int_bus)
        bus_delay.append(num)

delay_index = 1
bus_step = real_buses[0]

departure_bus = 0
valid_departure = False

while not valid_departure:
    if delay_index == len(real_buses):
        valid_departure = True
    else:
        departure_bus += bus_step
        attempting_departure = (departure_bus + bus_delay[delay_index]) % real_buses[delay_index] == 0
        if attempting_departure:
            bus_step *= real_buses[delay_index]
            print('step changed to ' + str(bus_step) + ' at the minute ' + str(departure_bus))
            delay_index += 1

print(departure_bus)

exit(0)
