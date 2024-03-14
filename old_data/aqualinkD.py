import json
import requests


'''# Opening JSON file
f = open('temps.json')

# returns JSON object as
# a dictionary
data = json.load(f)'''


with open("aqua_statuses.json", "r") as file:
    jsonData = json.load(file)

print("Type of JSON Object: ", type(jsonData))

for i in jsonData:
    print(i)
    # print(i["type"])
    # print(i["id"])
    # print(i["name"])
    # print(i["state"])
    # print(i["sp_value"])
    # print(i["int_status"])


'''# Traversing the json file
for name in jsonData:
    print("Name: ", name)
    print("Phone Number: ", jsonData[name]["number"])
    print("Age: ", jsonData[name]["age"])

    print("Address:")
    for line in jsonData[name]["address"]:
        print(line)
    print()'''


'''
data = {
    "type": "switch",
    "id": "Aux_5",
    "name": "Spa Light",
    "state": "off",
    "status": "off",
    "int_status": "0",
    "type_ext": "switch_program",
    "Light_Type": "2"
},
{
    "type": "switch",
    "id": "Aux_6",
    "name": "Fountain Light",
    "state": "off",
    "status": "off",
    "int_status": "0",
    "type_ext": "switch_program",
    "Light_Type": "2"
}
{
    "type": "switch",
    "id": "Aux_7",
    "name": "Heater",
    "state": "off",
    "status": "off",
    "int_status": "0",
    "type_ext": "switch_timer",
    "timer_active": "off"
},
{
    "type": "setpoint_thermo",
    "id": "Pool_Heater",
    "name": "Solar",
    "state": "off",
    "status": "off",
    "spvalue": "36",
    "value": "68",
    "int_status": "0",
    "timer_active": "off"
},
{
    "type": "setpoint_thermo",
    "id": "Spa_Heater",
    "name": "Spa Heater",
    "state": "off",
    "status": "off",
    "spvalue": "36",
    "value": "-999",
    "int_status": "0",
    "timer_active": "off"
},
{
    "type": "switch",
    "id": "Solar_Heater",
    "name": "Solar Heater",
    "state": "off",
    "status": "off",
    "int_status": "0",
    "type_ext": "switch_timer",
    "timer_active": "off"
},
{
    "type": "setpoint_freeze",
    "id": "Freeze_Protect",
    "name": "Freeze Protection",
    "state": "off",
    "status": "enabled",
    "spvalue": "38",
    "value": "69",
    "int_status": "0"
},
{
    "type": "setpoint_swg",
    "id": "SWG",
    "name": "Salt Water Generator",
    "state": "on",
    "status": "on",
    "spvalue": "95",
    "value": "95",
    "int_status": "1"
},
{
    "type": "value",
    "id": "SWG/Percent",
    "name": "Salt Water Generator Percent",
    "state": "on",
    "value": "95"
},
{
    "type": "switch",
    "id": "SWG/Boost",
    "name": "SWG Boost",
    "state": "off",
    "status": "off",
    "int_status": "0"
},
{
    "type": "value",
    "id": "SWG/PPM",
    "name": "Salt Level PPM",
    "state": "on",
    "value": "1700"
},
{
    "type": "temperature",
    "id": "Temperature/Air",
    "name": "Pool Air Temperature",
    "state": "on",
    "value": "69"
},
{
    "type": "temperature",
    "id": "Temperature/Pool",
    "name": "Pool Water Temperature",
    "state": "on",
    "value": "68"
},
{
    "type": "temperature",
    "id": "Temperature/Spa",
    "name": "Spa Water Temperature",
    "state": "on",
    "value": "-999"
}


for i in data:
    print(i)





'''
