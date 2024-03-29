data = {
    "date": "03/02/24 SAT",
    "devices": [
        {
            "Pump_GPM": "0",
            "Pump_RPM": "0",
            "Pump_Type": "vsPump",
            "Pump_Watts": "0",
            "id": "Filter_Pump",
            "int_status": "1",
            "name": "Filter Pump",
            "state": "on",
            "status": "on",
            "type": "switch",
            "type_ext": "switch_vsp"
        },
        {
            "id": "Spa_Mode",
            "int_status": "0",
            "name": "Spa Mode",
            "state": "off",
            "status": "off",
            "timer_active": "off",
            "type": "switch",
            "type_ext": "switch_timer"
        },
        {
            "id": "Aux_1",
            "int_status": "1",
            "name": "Cleaner",
            "state": "on",
            "status": "on",
            "timer_active": "off",
            "type": "switch",
            "type_ext": "switch_timer"
        },
        {
            "id": "Aux_2",
            "int_status": "0",
            "name": "Fountain",
            "state": "off",
            "status": "off",
            "timer_active": "off",
            "type": "switch",
            "type_ext": "switch_timer"
        },
        {
            "id": "Aux_3",
            "int_status": "0",
            "name": "Blower",
            "state": "off",
            "status": "off",
            "timer_active": "off",
            "type": "switch",
            "type_ext": "switch_timer"
        },
        {
            "Light_Type": "2",
            "id": "Aux_4",
            "int_status": "0",
            "name": "Pool Light",
            "state": "off",
            "status": "off",
            "type": "switch",
            "type_ext": "switch_program"
        },
        {
            "Light_Type": "2",
            "id": "Aux_5",
            "int_status": "0",
            "name": "Spa Light",
            "state": "off",
            "status": "off",
            "type": "switch",
            "type_ext": "switch_program"
        },
        {
            "Light_Type": "2",
            "id": "Aux_6",
            "int_status": "0",
            "name": "Fountain Light",
            "state": "off",
            "status": "off",
            "type": "switch",
            "type_ext": "switch_program"
        },
        {
            "id": "Aux_7",
            "int_status": "0",
            "name": "Heater",
            "state": "off",
            "status": "off",
            "timer_active": "off",
            "type": "switch",
            "type_ext": "switch_timer"
        },
        {
            "id": "Pool_Heater",
            "int_status": "0",
            "name": "Solar",
            "spvalue": "36",
            "state": "off",
            "status": "off",
            "timer_active": "off",
            "type": "setpoint_thermo",
            "value": "68"
        },
        {
            "id": "Spa_Heater",
            "int_status": "0",
            "name": "Spa Heater",
            "spvalue": "36",
            "state": "off",
            "status": "off",
            "timer_active": "off",
            "type": "setpoint_thermo",
            "value": "-999"
        },
        {
            "id": "Solar_Heater",
            "int_status": "0",
            "name": "Solar Heater",
            "state": "off",
            "status": "off",
            "timer_active": "off",
            "type": "switch",
            "type_ext": "switch_timer"
        },
        {
            "id": "Freeze_Protect",
            "int_status": "0",
            "name": "Freeze Protection",
            "spvalue": "38",
            "state": "off",
            "status": "enabled",
            "type": "setpoint_freeze",
            "value": "69"
        },
        {
            "id": "SWG",
            "int_status": "1",
            "name": "Salt Water Generator",
            "spvalue": "95",
            "state": "on",
            "status": "on",
            "type": "setpoint_swg",
            "value": "95"
        },
        {
            "id": "SWG/Percent",
            "name": "Salt Water Generator Percent",
            "state": "on",
            "type": "value",
            "value": "95"
        },
        {
            "id": "SWG/Boost",
            "int_status": "0",
            "name": "SWG Boost",
            "state": "off",
            "status": "off",
            "type": "switch"
        },
        {
            "id": "SWG/PPM",
            "name": "Salt Level PPM",
            "state": "on",
            "type": "value",
            "value": "1700"
        },
        {
            "id": "Temperature/Air",
            "name": "Pool Air Temperature",
            "state": "on",
            "type": "temperature",
            "value": "69"
        },
        {
            "id": "Temperature/Pool",
            "name": "Pool Water Temperature",
            "state": "on",
            "type": "temperature",
            "value": "68"
        },
        {
            "id": "Temperature/Spa",
            "name": "Spa Water Temperature",
            "state": "on",
            "type": "temperature",
            "value": "-999"
        }
    ],
    "temp_units": "f",
    "time": "5:27 PM",
    "type": "devices"
}
"""print()
print("Pump Name: {}".format(data["devices"][8]["name"]))
print("Pump ID: {}".format(data["devices"][0]["id"]))
print("Pump GPM: {}".format(data["devices"][0]["Pump_GPM"]))
print("Pump RPM: {}".format(data["devices"][0]["Pump_RPM"]))
print("Pump Watts: {}".format(data["devices"][0]["Pump_Watts"]))
print("Pump Type: {}".format(data["devices"][0]["Pump_Type"]))
print("Status int: {}".format(data["devices"][0]["int_status"]))
print("Status: {}".format(data["devices"][2]["status"]))
print("State: {}".format(data["devices"][0]["state"]))"""

try:
    for i in data["devices"]:
        # print(i)
        # print(print("ID: {}".format(i["id"])))

        """if i["type"] == "temperature":
            print("Temperature")
            print(print("ID: {}".format(i["id"])))
            print(print("Name: {}".format(i["name"])))
            print(print("State: {}".format(i["state"])))
            print(print("Value: {}".format(i["value"])))
            print()"""

        """if i["type"] == "setpoint_thermo":
            print("Switch Heaters")
            print(print("ID: {}".format(i["id"])))
            print(print("Status int: {}".format(i["int_status"])))
            print(print("Name: {}".format(i["name"])))
            print(print("State: {}".format(i["state"])))
            print(print("Status: {}".format(i["status"])))
            print(print("Type External: {}".format(i["type_ext"])))
            print()"""

        if i["type_ext"] == "switch_program" or "switch_timer":
            print("Switch_EXT")
            print(print("ID: {}".format(i["id"])))
            print(print("Status int: {}".format(i["int_status"])))
            print(print("Name: {}".format(i["name"])))
            print(print("State: {}".format(i["state"])))
            print(print("Status: {}".format(i["status"])))
            print(print("Type External: {}".format(i["type_ext"])))
            print()

        """if i["type"] == "setpoint_thermo" or "setpoint_freeze" or "setpoint_swg":
            print("Setpoint")
            print(print("ID: {}".format(i["id"])))
            print(print("Status int: {}".format(i["int_status"])))
            print(print("Name: {}".format(i["name"])))
            print(print("Setpoint: Value: {}".format(i["spvalue"])))
            print(print("State: {}".format(i["state"])))
            print(print("Status: {}".format(i["status"])))
            print(print("Value: {}".format(i["value"])))
            print()

        if i["type"] == "value":
            print("Value")
            print(print("ID: {}".format(i["id"])))
            print(print("Name: {}".format(i["name"])))
            print(print("State: {}".format(i["state"])))
            print(print("Value: {}".format(i["value"])))

        if i["type_ext"] == "switch_vsp":
            print("Value")
            print(print("ID: {}".format(i["id"])))
            print(print("Name: {}".format(i["name"])))
            print(print("State: {}".format(i["state"])))
            # print(print("Value: {}".format(i["value"])))"""


except KeyError:
    print(f"Alert, Item not found! ")
