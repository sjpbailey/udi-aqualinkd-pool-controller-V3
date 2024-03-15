data = {
    "Pump_1": {
        "GPM": "0",
        "Pump_Type": "vsPump",
        "RPM": "0",
        "Watts": "0",
        "id": "Filter_Pump",
        "name": "Filter Pump"
    },
    "air_temp": "69",
    "aqualinkd_version": "2.3.2",
    "battery": "ok",
    "date": "03/02/24 SAT",
    "frz_protect_set_pnt": "38",
    "leds": {
        "Aux_1": "on",
        "Aux_2": "off",
        "Aux_3": "off",
        "Aux_4": "off",
        "Aux_5": "off",
        "Aux_6": "off",
        "Aux_7": "off",
        "Filter_Pump": "on",
        "Freeze_Protect": "enabled",
        "Pool_Heater": "off",
        "SWG": "on",
        "SWG/Boost": "off",
        "Solar_Heater": "off",
        "Spa_Heater": "off",
        "Spa_Mode": "off"
    },
    "panel_message": "AIR TEMP 69 F",
    "panel_type": "RS-8 Combo Pool/Spa",
    "pool_htr_set_pnt": "36",
    "pool_temp": "68",
    "spa_htr_set_pnt": "36",
    "spa_temp": " ",
    "status": "CHECK AquaPure LOW SALT HIGH SALT",
    "swg_fullstatus": "2",
    "swg_percent": "95",
    "swg_ppm": "1700",
    "temp_units": "f",
    "time": "5:27 PM",
    "timer_durations": {},
    "timers": {},
    "type": "status",
    "version": "E0260801 REV R"
}


print()
print("SWG: {}".format(data["leds"]["SWG"]))
print()
print("SWG Boost: {}".format(data["leds"]["SWG/Boost"]))
print()
print("SWG Present: {}".format(data["swg_percent"]))
print()
print("SWG PPM: {}".format(data["swg_ppm"]))

"""print()
print("Pump GPM {}".format(data["Pump_1"]["GPM"]))
print()
print("Pump RPM {}".format(data["Pump_1"]["RPM"]))
print()
print("Pump Watts {}".format(data["Pump_1"]["Watts"]))
print()
print("Pump ID {}".format(data["Pump_1"]["id"]))
print()
print("Pump Type {}".format(data["Pump_1"]["Pump_Type"]))

print()
print("Air Temp  {}".format(data["air_temp"]))
print()
print("Pool Temp  {}".format(data["pool_temp"]))
print()
print("Freeze Setpoint {}".format(data["frz_protect_set_pnt"]))
print()
print("Pool Heat Setpoint {}".format(data["pool_htr_set_pnt"]))
print()
print("Spa Heat Setpoint {}".format(data["spa_htr_set_pnt"]))
print()
print("Pump Status: {}".format(data["leds"]["Filter_Pump"]))
print()
print("Freeze Protection: {}".format(data["leds"]["Freeze_Protect"]))
print()
print("Pool Heater: {}".format(data["leds"]["Pool_Heater"]))

print()
print("Solar Heat: {}".format(data["leds"]["Solar_Heater"]))
print()
print("Spa Heat: {}".format(data["leds"]["Spa_Heater"]))
print()
print("Spa Mode: {}".format(data["leds"]["Spa_Mode"]))


print()
print("Auxillary 1: {}".format(data["leds"]["Aux_1"]))
print()
print("Auxillary 2: {}".format(data["leds"]["Aux_2"]))
print()
print("Auxillary 3: {}".format(data["leds"]["Aux_3"]))
print()
print("Auxillary 4: {}".format(data["leds"]["Aux_4"]))
print()
print("Auxillary 5: {}".format(data["leds"]["Aux_5"]))
print()
print("Auxillary 6: {}".format(data["leds"]["Aux_6"]))
print()
print("Auxillary 7: {}".format(data["leds"]["Aux_7"]))"""


# for i in data:
#    print(i[0])
