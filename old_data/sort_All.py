import json
import requests


################### Commands ###################################

###### Heating Setpoint ######
'''json_data = {
    "id": 1,
    # "name": "Pool",
    "heatSetpoint": '45',
}

response = requests.put(
    'http://192.168.1.53:4200/state/body/setPoint', json=json_data)

print()
print(response)
print(response.text)
if response.status_code == 200:
    print("Heat Setpoint")'''
'''
###### Pump Speed ######
json_data = {"id": 50, "circuits": [
    {"speed": 2200, "units": {"val": 0}, "id": 1, "circuit": 6}]}

response = requests.put(
    'http://192.168.1.53:4200/config/pump', json=json_data)

print()
print(response)
print(response.text)
if response.status_code == 200:
    print("Pump Speed")'''

'''
###### Pool Start/Stop ######
json_data = {"id": 6, "state": False}  # True-Start False-Stop

response = requests.put(
    'http://192.168.1.53:4200/state/circuit/setState', json=json_data)

print()
print(response)
print(response.text)
if response.status_code == 200:
    print("Start/Stop")'''

'''
###### Pump Status ######

response = requests.get('https://192.168.1.53:4200/config/options/pumps/')
print()
print(response)
print(response.text)
if response.status_code == 200:
    print("Pump Status?")'''


'''
###### Override Circuit ######

json_data = {
    'id': 2,
    'isOn': 0,
}

response = requests.put(
    'http://192.168.1.53:4200/state/circuit/setState/', json=json_data)'''


x = requests.get("http://192.168.1.55:4200/state/all/")
response = json.dumps(x.json(), indent=4, sort_keys=True)
# 'http://192.168.1.53:4200/config/circuits/'
# "http://192.168.1.53:4200/state/all/"'''
print(response)
# "http://192.168.1.53:4200/state/temps/"
# y = requests.get("http://192.168.1.53:4200/state/body/")
# print(y.text)
# response = (json.dumps(y.json(), indent=4, sort_keys=True))

# print(response)
for i in response:

    print("Name:  {}".format(i))

################ CIRCUITS ######################################
"""for i in y:
    print(i[0])  # ["name"], i["id"], i['isOn'])
print()
# ["temps"]["bodies"][0]["setPoint"]))
print("Setpoint {}".format(y["alias"]))
print()"""


# http://192.168.1.53:4200/state/all/systemUnits
# https://192.168.1.53:4201/state/pump/1/
# + [0]["bodies"])
# z = requests.get("http://192.168.1.53:4200/state/pumps/")
# print(json.dumps(z.json(), indent=4, sort_keys=True))
# print(z.text[0])
# print()

# z = requests.get("http://192.168.1.53:4200/state/filters/")
# print(json.dumps(z.json(), indent=4, sort_keys=True))
# print(z.text)
# print()


# print("Pool Running  {}".format(z["temps"]["bodies"][0]["isOn"]))
# q = requests.get('http://192.168.1.53:4200/state/temps/air')
# z = json.dumps(q.json(), indent=4, sort_keys=True)
# print("Setpoint Temp  {}".format(z["temps"]["bodies"][0]["setPoint"]))
# print(z)
# for i in z:
#    print(i)
# print(z.text)


# "http://192.168.1.53:4200/state/circuits/"
'''u = requests.get("http://192.168.1.53:4200/state/circuit/6/")
u = (json.dumps(u.json(), indent=4, sort_keys=True))
# print(u.text)
for i in u["circuits"]:
    print(i["name"])
    print(i["id"])
    print(i['isOn'])

# http://192.168.1.53:4200/config/options/heaters/

# http://192.168.1.53:4200/config/options/schedules/
# temps/bodies/[0]/setPoint
p = requests.get("http://192.168.1.53:4200/config/options/heaters/")
p = (json.dumps(p.json(), indent=4, sort_keys=True))
# print(p.text)
# "http://192.168.1.53:4200/config/options/schedules/"
# "http://192.168.1.53:4200/config/options/bodies/"
# '''
'''for i in p:
    print(i[0:1])
    print(i['name'])
    print(i['id'])
    print(i['type']['desc'])
    print(i['isOn'])
    # print(i['name'])'''

data = {
    "alias": "BackYard",
    "appVersion": "8.0.1",
    "appVersionState": {
        "equipmentType": "appVersion",
        "gitLocalBranch": "master",
        "gitLocalCommit": "a2e1e75549b1246b3757d7deb7f1ddabeb702d92",
        "githubRelease": "8.0.2",
        "installed": "8.0.1",
        "nextCheckTime": "2024-03-05T16:44:00.244-0800",
        "status": {
            "desc": "New version available",
            "name": "behind",
            "val": 1
        }
    },
    "batteryVoltage": 0,
    "chemControllers": [],
    "chemDosers": [],
    "chlorinators": [],
    "circuitGroups": [],
    "circuits": [
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-03-05T19:35:21.770-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 6,
            "isActive": True,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Pool",
            "priority": "manual",
            "showInFeatures": True,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "body": 1,
                "desc": "Pool",
                "hasHeatSource": True,
                "name": "pool",
                "val": 12
            }
        },
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-03-05T01:49:54.007-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 2,
            "isActive": True,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Light",
            "showInFeatures": True,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "desc": "Light",
                "isLight": True,
                "name": "light",
                "val": 4
            }
        },
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-03-04T15:34:55.333-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 3,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Skim",
            "showInFeatures": True,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "desc": "Generic",
                "name": "generic",
                "val": 0
            }
        },
        {
            "action": {
                "desc": "Ready",
                "name": "ready",
                "val": 0
            },
            "endTime": "2024-03-04T15:31:41.570-0800",
            "equipmentType": "circuit",
            "freezeProtect": False,
            "id": 4,
            "isOn": False,
            "manualPriorityActive": False,
            "name": "Sweep",
            "showInFeatures": True,
            "startDelay": False,
            "stopDelay": False,
            "type": {
                "desc": "Generic",
                "name": "generic",
                "val": 0
            }
        }
    ],
    "clockMode": {
        "name": "12 Hour",
        "val": 12
    },
    "clockSource": {
        "desc": "Server",
        "name": "server",
        "val": 3
    },
    "controllerType": "nixie",
    "covers": [],
    "delay": {},
    "delays": [],
    "equipment": {
        "bootLoaderVersion": "",
        "controllerType": "nixie",
        "dual": False,
        "equipmentType": "equipment",
        "maxBodies": 1,
        "maxCircuitGroups": 16,
        "maxCircuits": 40,
        "maxFeatures": 32,
        "maxHeaters": 16,
        "maxLightGroups": 16,
        "maxPumps": 16,
        "maxSchedules": 100,
        "maxValves": 32,
        "messages": [],
        "model": "Nixie Single Body",
        "shared": False,
        "single": True,
        "softwareVersion": "1.0.0"
    },
    "features": [],
    "filters": [
        {
            "body": {
                "desc": "Pool",
                "name": "pool",
                "val": 0
            },
            "cleanPercentage": 100,
            "equipmentType": "filter",
            "filterType": {
                "desc": "Cartridge",
                "hasBackwash": False,
                "name": "cartridge",
                "val": 1
            },
            "id": 1,
            "isOn": False,
            "name": "Filter 1",
            "pressure": 0,
            "pressureUnits": {
                "desc": "Pounds per Sqare Inch",
                "name": "psi",
                "val": 0
            },
            "refPressure": 0
        }
    ],
    "freeze": False,
    "heaters": [
        {
            "bodyId": 0,
            "endTime": "2024-03-05T15:35:06.278-0800",
            "equipmentType": "heater",
            "id": 256,
            "isOn": False,
            "name": "Gas Heater 1",
            "shutdownDelay": False,
            "startTime": "2024-03-05T14:20:54.956-0800",
            "startupDelay": False,
            "type": {
                "desc": "Gas Heater",
                "hasAddress": False,
                "name": "gas",
                "val": 1
            }
        }
    ],
    "lightGroups": [],
    "mode": {
        "desc": "Auto",
        "name": "auto",
        "val": 0
    },
    "model": "Nixie Single Body",
    "nextSunrise": "2024-03-06T14:18:55.000-0800",
    "nextSunset": "2024-03-06T01:53:56.000-0800",


    "pumps": [
        {
            "address": 96,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-05T19:35:21.770-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "speed": 2250,
                    "units": {
                        "desc": "RPM",
                        "name": "rpm",
                        "val": 0
                    }
                }
            ],
            "command": 4,
            "driveState": 255,
            "equipmentType": "pump",
            "flow": 0,
            "id": 50,
            "isActive": True,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 15,
            "minSpeed": 450,
            "mode": 0,
            "name": "Pump 1",
            "ppc": 0,
            "pumpOnDelay": False,
            "rpm": 0,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "time": 944,
            "type": {
                "desc": "Intelliflo VSF",
                "hasAddress": True,
                "maxCircuits": 8,
                "maxFlow": 130,
                "maxSpeed": 3450,
                "minFlow": 15,
                "minSpeed": 450,
                "name": "vsf",
                "val": 4
            },
            "watts": 0
        },


        {
            "address": 97,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-05T19:35:21.770-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "speed": 3400,
                    "units": {
                        "desc": "RPM",
                        "name": "rpm",
                        "val": 0
                    }
                }
            ],
            "equipmentType": "pump",
            "id": 51,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 0,
            "minSpeed": 450,
            "name": "Pump 2",
            "pumpOnDelay": False,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "type": {
                "desc": "Intelliflo VS",
                "hasAddress": True,
                "maxCircuits": 8,
                "maxPrimingTime": 6,
                "maxSpeed": 3450,
                "minSpeed": 450,
                "name": "vs",
                "val": 3
            }
        },



        {
            "address": 98,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-05T19:35:21.770-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "flow": 124,
                    "id": 1,
                    "master": 1,
                    "units": {
                        "desc": "GPM",
                        "name": "gpm",
                        "val": 1
                    }
                }
            ],
            "equipmentType": "pump",
            "id": 52,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 15,
            "minSpeed": 450,
            "name": "Pump 3",
            "pumpOnDelay": False,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "type": {
                "desc": "Intelliflo VF",
                "hasAddress": True,
                "maxCircuits": 8,
                "maxFlow": 130,
                "minFlow": 15,
                "name": "vf",
                "val": 5
            }
        },



        {
            "address": 99,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-06T01:51:22.706-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "relay": 1,
                    "units": "undefined"
                }
            ],
            "equipmentType": "pump",
            "id": 53,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 0,
            "minSpeed": 0,
            "name": "Pump 4",
            "pumpOnDelay": False,
            "relay": 0,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "type": {
                "desc": "Single Speed",
                "hasAddress": False,
                "hasBody": False,
                "maxCircuits": 8,
                "maxRelays": 1,
                "name": "ss",
                "relays": [
                    {
                        "id": 1,
                        "name": "Pump On/Off"
                    }
                ],
                "val": 1
            }
        },


        {
            "address": 100,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-06T01:51:22.706-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "relay": 1,
                    "units": "undefined"
                }
            ],
            "equipmentType": "pump",
            "id": 54,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 0,
            "minSpeed": 0,
            "name": "Pump 5",
            "pumpOnDelay": False,
            "relay": 0,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "type": {
                "desc": "Two Speed",
                "hasAddress": False,
                "hasBody": False,
                "maxCircuits": 8,
                "maxRelays": 2,
                "name": "ds",
                "relays": [
                    {
                        "id": 1,
                        "name": "Low Speed"
                    },
                    {
                        "id": 2,
                        "name": "High Speed"
                    }
                ],
                "val": 2
            }
        },


        {
            "address": 101,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-06T01:51:22.706-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "speed": 3450,
                    "units": {
                        "desc": "RPM",
                        "name": "rpm",
                        "val": 0
                    }
                }
            ],
            "command": 0,
            "equipmentType": "pump",
            "id": 55,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 0,
            "minSpeed": 450,
            "name": "Pump 6",
            "pumpOnDelay": False,
            "rpm": 0,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "type": {
                "desc": "Hayward Eco/TriStar VS",
                "hasAddress": True,
                "maxCircuits": 8,
                "maxSpeed": 3450,
                "minSpeed": 450,
                "name": "hwvs",
                "val": 6
            },
            "watts": 0
        },


        {
            "address": 100,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-06T01:51:22.706-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "relay": 1,
                    "units": "undefined"
                }
            ],
            "command": 0,
            "driveState": 0,
            "equipmentType": "pump",
            "id": 56,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 0,
            "minSpeed": 0,
            "name": "Pump 7",
            "pumpOnDelay": False,
            "relay": 0,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "type": {
                "desc": "Hayward Relay VS",
                "hasAddress": False,
                "maxCircuits": 8,
                "maxRelays": 4,
                "maxSpeeds": 8,
                "name": "hwrly",
                "relays": [
                    {
                        "id": 1,
                        "name": "Step #1"
                    },
                    {
                        "id": 2,
                        "name": "Step #2"
                    },
                    {
                        "id": 3,
                        "name": "Step #3"
                    },
                    {
                        "id": 4,
                        "name": "Pump On"
                    }
                ],
                "val": 7
            }
        },

        {
            "address": 102,
            "circuits": [
                {
                    "circuit": {
                        "action": {
                            "desc": "Ready",
                            "name": "ready",
                            "val": 0
                        },
                        "endTime": "2024-03-06T00:38:44.114-0800",
                        "equipmentType": "circuit",
                        "freezeProtect": False,
                        "id": 6,
                        "isActive": True,
                        "isOn": False,
                        "manualPriorityActive": False,
                        "name": "Pool",
                        "priority": "manual",
                        "showInFeatures": True,
                        "startDelay": False,
                        "stopDelay": False,
                        "type": {
                            "body": 1,
                            "desc": "Pool",
                            "hasHeatSource": True,
                            "name": "pool",
                            "val": 12
                        }
                    },
                    "id": 1,
                    "master": 1,
                    "relay": 1,
                    "units": "undefined"
                }
            ],
            "equipmentType": "pump",
            "id": 57,
            "maxFlow": 130,
            "maxSpeed": 3450,
            "minFlow": 0,
            "minSpeed": 0,
            "name": "Pump 8",
            "pumpOnDelay": False,
            "relay": 0,
            "status": {
                "desc": "Ok",
                "name": "ok",
                "val": 0
            },
            "type": {
                "desc": "SuperFlo VS",
                "equipmentMaster": 1,
                "hasAddress": False,
                "maxCircuits": 8,
                "maxRelays": 4,
                "maxSpeeds": 4,
                "name": "sf",
                "relays": [
                    {
                        "id": 1,
                        "name": "Program #1"
                    },
                    {
                        "id": 2,
                        "name": "Program #2"
                    },
                    {
                        "id": 3,
                        "name": "Program #3"
                    },
                    {
                        "id": 4,
                        "name": "Program #4"
                    }
                ],
                "val": 100
            }
        }




    ],

    "schedules": [
        {
            "circuit": {
                "action": {
                    "desc": "Ready",
                    "name": "ready",
                    "val": 0
                },
                "endTime": "2024-03-05T19:35:21.770-0800",
                "equipmentType": "circuit",
                "freezeProtect": False,
                "id": 6,
                "isActive": True,
                "isOn": False,
                "manualPriorityActive": False,
                "name": "Pool",
                "priority": "manual",
                "showInFeatures": True,
                "startDelay": False,
                "stopDelay": False,
                "type": {
                    "body": 1,
                    "desc": "Pool",
                    "hasHeatSource": True,
                    "name": "pool",
                    "val": 12
                }
            },
            "clockMode": {
                "name": "12 Hour",
                "val": 12
            },
            "coolSetpoint": 100,
            "display": {
                "desc": "Always",
                "name": "always",
                "val": 0
            },
            "endTime": 840,
            "endTimeType": {
                "desc": "Manual",
                "name": "manual",
                "val": 0
            },
            "equipmentType": "schedule",
            "heatSetpoint": 78,
            "heatSource": {
                "desc": "Heater",
                "name": "heater",
                "val": 2
            },
            "id": 1,
            "isOn": False,
            "manualPriorityActive": False,
            "scheduleDays": {
                "days": [
                    {
                        "bitval": 64,
                        "desc": "Sunday",
                        "dow": 0,
                        "name": "sun"
                    },
                    {
                        "bitval": 32,
                        "desc": "Saturday",
                        "dow": 6,
                        "name": "sat"
                    },
                    {
                        "bitval": 16,
                        "desc": "Friday",
                        "dow": 5,
                        "name": "fri"
                    },
                    {
                        "bitval": 8,
                        "desc": "Thursday",
                        "dow": 4,
                        "name": "thu"
                    },
                    {
                        "bitval": 4,
                        "desc": "Wednesday",
                        "dow": 3,
                        "name": "wed"
                    },
                    {
                        "bitval": 2,
                        "desc": "Tuesday",
                        "dow": 2,
                        "name": "tue"
                    },
                    {
                        "bitval": 1,
                        "desc": "Monday",
                        "dow": 1,
                        "name": "mon"
                    }
                ],
                "val": 127
            },
            "scheduleTime": {
                "calculated": True,
                "calculatedDate": "2024-03-05T00:00:00.000-0800",
                "endTime": "2024-03-05T14:00:59.999-0800",
                "shouldBeOn": False,
                "startTime": "2024-03-05T10:00:00.000-0800"
            },
            "scheduleType": {
                "days": "multi",
                "desc": "Repeats",
                "endTime": True,
                "heatSetpoint": True,
                "heatSource": True,
                "name": "repeat",
                "startDate": False,
                "startTime": True,
                "val": 128
            },
            "startDate": "2024-02-02T00:00:00.000-0800",
            "startTime": 600,
            "startTimeType": {
                "desc": "Manual",
                "name": "manual",
                "val": 0
            },
            "triggered": False
        }
    ],
    "startTime": "2024-03-03T10:15:59.429-0800",
    "status": {
        "desc": "Ready",
        "name": "ready",
        "percent": 100,
        "val": 1
    },
    "sunrise": "2024-03-05T14:20:21.000-0800",
    "sunset": "2024-03-05T01:52:58.000-0800",
    "systemUnits": {
        "desc": "English",
        "name": "english",
        "val": 0
    },
    "temps": {
        "air": 53.43,
        "bodies": [
            {
                "circuit": 6,
                "heatMode": {
                    "desc": "Heater",
                    "name": "heater",
                    "val": 2
                },
                "heatStatus": {
                    "desc": "Off",
                    "name": "off",
                    "val": 0
                },
                "heaterCooldownDelay": False,
                "heaterOptions": {
                    "gas": 1,
                    "heatpump": 0,
                    "hybrid": 0,
                    "mastertemp": 0,
                    "maxetherm": 0,
                    "solar": 0,
                    "total": 1,
                    "ultratemp": 0
                },
                "id": 1,
                "isCovered": False,
                "isOn": False,
                "name": "Pool",
                "setPoint": 78,
                "showInDashboard": True,
                "startDelay": False,
                "stopDelay": False,
                "temp": 55.62,
                "type": {
                    "desc": "Pool",
                    "name": "pool",
                    "val": 0
                }
            }
        ],
        "equipmentType": "temps",
        "units": {
            "desc": "Fahrenheit",
            "name": "F",
            "val": 0
        },
        "waterSensor1": 55.62,
        "waterSensor2": 54.73,
        "waterSensor3": 11.33
    },
    "time": "2024-03-05T15:43:00.600-0800",
    "valve": 0,
    "valveMode": {},
    "valves": [
        {
            "equipmentType": "valve",
            "id": 50,
            "isActive": True,
            "isDiverted": False,
            "isIntake": False,
            "isReturn": False,
            "name": "Valve Skim",
            "pinId": 0,
            "type": {
                "desc": "Standard",
                "name": "standard",
                "val": 0
            }
        },
        {
            "equipmentType": "valve",
            "id": 51,
            "isActive": True,
            "isDiverted": False,
            "isIntake": False,
            "isReturn": False,
            "name": "Valve Sweep",
            "pinId": 0,
            "type": {
                "desc": "Standard",
                "name": "standard",
                "val": 0
            }
        }
    ],
    "virtualCircuits": [
        {
            "equipmentType": "virtualCircuit",
            "id": 244,
            "isActive": True,
            "isOn": False,
            "name": "Pool Heater",
            "type": {
                "desc": "Pool Heater",
                "name": "poolHeater",
                "val": 244
            }
        },
        {
            "equipmentType": "virtualCircuit",
            "id": 246,
            "isActive": True,
            "isOn": False,
            "name": "Freeze",
            "type": {
                "desc": "Freeze",
                "name": "freeze",
                "val": 246
            }
        },
        {
            "equipmentType": "virtualCircuit",
            "id": 247,
            "isActive": True,
            "isOn": False,
            "name": "Pool/Spa",
            "type": {
                "desc": "Pool/Spa",
                "name": "poolSpa",
                "val": 247
            }
        },
        {
            "equipmentType": "virtualCircuit",
            "id": 258,
            "isActive": True,
            "isOn": False,
            "name": "Any Heater",
            "type": {
                "desc": "Any Heater",
                "name": "anyHeater",
                "val": 258
            }
        }
    ]
}


############### PUMPS ##################
# Pump  addressing if more than one pump
# 96 = 1 = 0
# 97 = 2 = 1
# 98 = 3 = 2
# 99 = 4 = 3

# PLUS circuit "id": 50 for Pump 1 / "id": 51 for Pump 2


'''###### PUMP 1 VSF ######
# print()
# print("Pumps  {}".format(data["pumps"][0]))
print()
print("Name  {}".format(data["pumps"][0]["name"]))
print()
print("Address  {}".format(data["pumps"][0]["address"]))
print()
print("Type  {}".format(data["pumps"][0]["type"]['desc']))
print()
print("Status  {}".format(data["pumps"][0]["circuits"][0]['circuit']['isOn']))
print()
# Watts for all pumps ADD 1 - 96!
print("Watts  {}".format(data["pumps"][0]["watts"]))
print()
print("RPM  {}".format(data["pumps"][0]["rpm"]))
print()
# GPM FOR ALL PUMPS AT ADD 1 - 96!
print("GPM  {}".format(data["pumps"][0]["flow"]))
print()
print("RPM Setpoint  {}".format(data["pumps"][0]["circuits"][0]["speed"]))
print()
print("Min Speed  {}".format(data["pumps"][0]["type"]['minSpeed']))
print()
print("Max Speed  {}".format(data["pumps"][0]["type"]['maxSpeed']))
print()
print("Min GPM  {}".format(data["pumps"][0]["type"]['minFlow']))
print()
print("Max GPM  {}".format(data["pumps"][0]["type"]['maxFlow']))
print()
# print("RPM  {}".format(data["pumps"][0]["circuits"][0]["units"]['val']))
# print()
# print("Circuit  {}".format(data["pumps"][0]["circuits"][0]))
# print()


###### PUMP 2 VS ######
print()
# print("Pumps  {}".format(data["pumps"][1]))
# print()
print("Name  {}".format(data["pumps"][1]["name"]))
print()
print("Address  {}".format(data["pumps"][1]["address"]))
print()
print("Type  {}".format(data["pumps"][1]["type"]['desc']))
print()
print("Status  {}".format(data["pumps"][1]["circuits"][0]['circuit']['isOn']))
print()
# Watts for all pumps ADD 1 - 96!
print("Watts  {}".format(data["pumps"][0]["watts"]))
print()
print("RPM  {}".format(data["pumps"][1]["circuits"][0]['units']['val']))
print()
# GPM from address 1 - 96
print("GPM  {}".format(data["pumps"][0]["flow"]))
print()
print("RPM Setpoint  {}".format(data["pumps"][1]["circuits"][0]["speed"]))
print()
print("Min Speed  {}".format(data["pumps"][1]["type"]['minSpeed']))
print()
print("Max Speed  {}".format(data["pumps"][1]["type"]['maxSpeed']))
print()
print("Min GPM  {}".format(data["pumps"][1]['minFlow']))
print()
print("Max GPM  {}".format(data["pumps"][1]['maxFlow']))
print()
# print("Circuit  {}".format(data["pumps"][1]["circuits"][0]))
# print()
#'''

'''###### PUMP 3 VF ######
# print()
# print("Pumps  {}".format(data["pumps"][1]))
print()
print("Name  {}".format(data["pumps"][2]["name"]))
print()
print("Address  {}".format(data["pumps"][2]["address"]))
print()
print("Type  {}".format(data["pumps"][2]["type"]['desc']))
print()
print("Status  {}".format(data["pumps"][2]["circuits"][0]['circuit']['isOn']))
print()

# Watts for all pumps ADD 1 - 96!
print("Watts  {}".format(data["pumps"][0]["watts"]))
print()
print("RPM  {}".format(data["pumps"][2]["circuits"][0]['units']['val']))
print()
# GPM from address 1 - 96
print("GPM  {}".format(data["pumps"][0]["flow"]))
print()
print("GPM Setpoint  {}".format(data["pumps"][2]["circuits"][0]["flow"]))
print()
print("Min Speed {}".format(data["pumps"][2]['minSpeed']))
print()
print("Max Speed {}".format(data["pumps"][2]['maxSpeed']))
print()
print("Min Flow  {}".format(data["pumps"][2]["minFlow"]))
print()
print("Max Flow  {}".format(data["pumps"][2]["maxFlow"]))
print()
# print("Circuit  {}".format(data["pumps"][1]["circuits"][0]))
# print()'''


'''###### PUMP 3 VF ######
# print()
# print("Pumps  {}".format(data["pumps"][1]))
print()
print("Name  {}".format(data["pumps"][3]["name"]))
print()
print("Address  {}".format(data["pumps"][3]["address"]))
print()
print("Type  {}".format(data["pumps"][3]["type"]['desc']))
print()
print("Status  {}".format(data["pumps"][3]["circuits"][0]['circuit']['isOn']))
print()

# Watts for all pumps ADD 1 - 96!
print("Watts  {}".format(data["pumps"][0]["watts"]))
print()
print("RPM  {}".format(data["pumps"][3]["circuits"]))  # ['units']['val']))
print()
# GPM from address 1 - 96
print("GPM  {}".format(data["pumps"][0]["flow"]))
print()
# print("GPM Setpoint  {}".format(data["pumps"][3]["circuits"][0]["flow"]))
# print()
print("Min Speed {}".format(data["pumps"][3]['minSpeed']))
print()
print("Max Speed {}".format(data["pumps"][3]['maxSpeed']))
print()
print("Min Flow  {}".format(data["pumps"][3]["minFlow"]))
print()
print("Max Flow  {}".format(data["pumps"][3]["maxFlow"]))
print()
# print("Circuit  {}".format(data["pumps"][1]["circuits"][0]))
# print()'''


# start relay for vs super
# {method: 'put', url: '/config/pump', data: '{"id":51,"circuits":[{"relay":3,"units":{"val":null},"id":1,"circuit":6}]}'}data: "{\"id\":51,\"circuits\":[{\"relay\":3,\"units\":{\"val\":null},\"id\":1,\"circuit\":6}]}"method: "put"url: "/config/pump"[[Prototype]]: Object
# data:"{\"id\":50,\"circuits\":[{\"relay\":3,\"units\":{\"val\":null},\"id\":1,\"circuit\":6}]}"
'''print()
for i in data["pumps"]:

    print("Name:  {}".format(i["name"]))
    # , i["rpm"], i["circuits"][0], i["name"])
    print("Address:  {}".format(i["address"]))
    print("ID:  {}".format(i["id"]))
    print("Type:  {}".format(i["type"]['desc']))
    print("Status:  {}".format(i["circuits"][0]['circuit']['isOn']))
    # print("RPM!  {}".format(i[0]["circuits"][0]['units']['val']))
    # print(i['watts'])
    # print(i["flow"])
    # print(i["minSpeed"])
    # print(i["maxSpeed"])
    # print(i["minFlow"])
    # print(i["minFlow"])
    try:
        print("Watts:!  {}".format(i['watts']))
    except KeyError:
        pass
        print('NO Watts')
    try:
        print("RPM:!  {}".format(data["pumps"][0]["rpm"]))
    except KeyError:
        pass
        print('NO RPM')
    try:
        print("GPM:!  {}".format(i['flow']))
        print()
        print()
    except KeyError:
        pass
        print('NO GPM')
        print()
        print()'''

'''
    try:
        print("RPM!  {}".format(i[0]["circuits"][0]['units']['val']))
    except KeyError:
        pass
        print('NO RPM')

    # print(i["circuits"][0])
    # print(i["rpm"])
    if i["type"]['desc'] == "Intelliflo VSF":
        print("Intelliflo VSF")
    if i["type"]['desc'] == "Intelliflo VS":
        print("Intelliflo VS")
    if i["type"]['desc'] == "Intelliflo VF":
        print("Intelliflo VF")
    if i["type"]['desc'] == "Single Speed":
        print("Single Speed")
    if i["type"]['desc'] == "Two Speed":
        print("Two Speed")
    if i["type"]['desc'] == "Hayward Eco/TriStar VS":
        print("Hayward Eco/TriStar VS")
    if i["type"]['desc'] == "Hayward Relay VS":
        print("Hayward Relay VS")
    if i["type"]['desc'] == "SuperFlo VS":
        print("SuperFlo VS")
'''
'''
# Virtual Circuits ######
print()
# ["bodies"][0]["temp"]))
print("Pool Temp  {}".format(data["virtualCircuits"]))
print()

for i in data["virtualCircuits"]:
    print(i['name'])
    print(i['id'])
    print(i['isOn'])
    # print(i['name'])


###### Heaters ######
print()
# ["bodies"][0]["temp"]))
print("Pool Temp  {}".format(data["heaters"]))
print()
for i in data["heaters"]:
    print(i['name'])
    print(i['id'])
    print(i['type']['desc'])
    print(i['isOn'])
    # print(i['name'])
'''


'''
print()
# print("Filter PSI {}".format(data["filters"][0]["pressure"]))
print()
print()
print("Filter PSI {}".format(data["heaters"]))
print()
print()
print("Setpoint {}".format(data["temps"]["bodies"][0]))
print("App Version {}".format(data["appVersion"]))
print()
print("Setpoint {}".format(data["temps"]["bodies"][0]))


print()
print()
# print("Schedule {}".format(data["schedules"][0]))
# print("Bodies {}".format(data["config"]["options"]))  # [0]["setPoint"]))


print()
print("App Version {}".format(data["appVersionState"]))
print()
print("Battery Voltage {}".format(data["batteryVoltage"]))
print()
print("Chemical Controllers {}".format(data["chemControllers"]))
print()
print("Chemical Dosers {}".format(data["chemDosers"]))
print()
print("Chlorinators {}".format(data["chlorinators"]))
print()
print("Circuit Groups {}".format(data["circuitGroups"]))
print()
print("Pool Temp  {}".format(data["temps"]["bodies"][0]["temp"]))
print()
print("Setpoint Temp  {}".format(data["temps"]["bodies"][0]["setPoint"]))
print()
print("Pool Running  {}".format(data["temps"]["bodies"][0]["isOn"]))
print()
# ["action"]))
# print("Circuits {}".format(data["circuits"]
#      [0]["name"]))
# print("Circuits {}".format(data["circuits"][1]["name"]))
# print("Circuits {}".format(data["circuits"][2]["name"]))
# print("Circuits {}".format(data["circuits"][3]["name"]))
# print("Circuits {}".format(data["circuits"][0]["id"]))
print()
print("Air Temp  {}".format(data["temps"]["air"]))"""
print()
print("Setpoint Temp  {}".format(data["temps"]["bodies"][0]["setPoint"]))
print()
print("Pool Temp  {}".format(data["temps"]["bodies"][0]["temp"]))
print()
# print("Pumps  {}".format(data["pumps"]))
print()
# print("Filters  {}".format(data["filters"]))
print()
# print("Valves  {}".format(data["valves"]))
print()
# print("Virtual Circuits  {}".format(data["virtualCircuits"]))
print()
print("Heater {}".format(data["heaters"]))
print()
# print("Schedule {}".format(data["schedules"][0]))
# print()
# ["name"]))
# [0]["circuits"]["circuit"]["name"]))
print("Circuit On {}".format(data["circuits"][3]['isOn']))
################ CIRCUITS ######################################
for i in data["circuits"]:
    print(i["name"])
    print(i["id"])
    print(i['isOn'])
print("Circuit On {}".format(data["circuits"][0]['isOn']))
#      [0]["name"]))

print()
print("Air Temp {}".format(data["air"]))
print()
print("Water Temp {}".format(data["waterSensor1"]))
print()

print("Circuit {}".format(data["bodies"][0]["circuit"]))
print("ID {}".format(data["bodies"][0]["id"]))
print("Heater Name {}".format(data["bodies"][0]["heatMode"]["name"]))
print()
print("Setpoint {}".format(data["bodies"][0]["setPoint"]))
print("Temperature {}".format(data["bodies"][0]["temp"]))
print()

print("Heat Options Gas {}".format(data["bodies"][0]["heaterOptions"]["gas"]))
print()
print("Heat Options HeatPump {}".format(
    data["bodies"][0]["heaterOptions"]["heatpump"]))
print()
print("Heat Options Hybrid {}".format(
    data["bodies"][0]["heaterOptions"]["hybrid"]))
print()
print("Heat Options MasterTemp {}".format(
    data["bodies"][0]["heaterOptions"]["mastertemp"]))
print()
print("Heat Options Maxetherm {}".format(
    data["bodies"][0]["heaterOptions"]["maxetherm"]))
print()
print("Heat Options Solar {}".format(
    data["bodies"][0]["heaterOptions"]["solar"]))
print()
print("Heat Options Ultratemp {}".format(
    data["bodies"][0]["heaterOptions"]["ultratemp"]))
print()
print("Total Heaters {}".format(data["bodies"][0]["heaterOptions"]["total"]))
print()
# print(data["bodies"][0])


# print(data["heater"]["name"])
# print(data["setpoint"])


# Closing file
# f.close()

'''
