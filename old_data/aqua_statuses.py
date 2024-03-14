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
print("Pump Type {}".format(data["frz_protect_set_pnt"]))


# for i in data:
#    print(i[0])
